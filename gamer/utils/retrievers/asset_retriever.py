"""DocDB retriever class that communicates with MongoDB"""

import asyncio
import json
from typing import Any, List, Optional

import boto3
from aind_data_access_api.document_db import MetadataDbClient
from bson import json_util
from langchain_aws import BedrockEmbeddings
from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from pydantic import Field

BEDROCK_CLIENT = boto3.client(
    service_name="bedrock-runtime", region_name="us-west-2"
)

BEDROCK_EMBEDDINGS = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0", client=BEDROCK_CLIENT
)

API_GATEWAY_HOST = "api.allenneuraldynamics-test.org"
DATABASE = "metadata_vector_index"
COLLECTION = "TITAN_4096_all"

docdb_api_client = MetadataDbClient(
    host=API_GATEWAY_HOST,
    database=DATABASE,
    collection=COLLECTION,
)


class DocDBRetriever(BaseRetriever):
    """
    A retriever that contains the top k documents,
    retrieved from the DocDB index,
    aligned with the user's query.
    """

    # collection: Any = Field(description="DocDB collection to retrieve from")
    k: int = Field(default=5, description="Number of documents to retrieve")

    def _get_relevant_documents(
        self,
        query: str,
        query_filter: dict,
        run_manager: Optional[CallbackManagerForRetrieverRun] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """
        Synchronous call to retrieve relevant docs from MongoDB
        """

        raise NotImplementedError("Use _aget_relevant_documents for async contexts")

    async def _aget_relevant_documents(
        self,
        query: str,
        query_filter: Optional[dict] = None,
        run_manager: Optional[CallbackManagerForRetrieverRun] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """
        Async call
        """

        # Embed query

        embedded_query = await BEDROCK_EMBEDDINGS.aembed_query(query)

        # Construct aggregation pipeline
        vector_search = {
            "$search": {
                "vectorSearch": {
                    "vector": embedded_query,
                    "path": "vectorContent",
                    "similarity": "euclidean",
                    "k": self.k,
                    "efSearch": 250,
                }
            }
        }

        projection_stage = {"$project": {"textContent": 1}}

        pipeline = [vector_search, projection_stage]
        if query_filter:
            if "$match" not in query_filter:
                query_filter = {"$match": query_filter}
            pipeline.insert(0, query_filter)

        try:
            result = docdb_api_client.aggregate_docdb_records(
                pipeline=pipeline
            )

            # async def process_document(document):
            #     """
            #     Converting retrieved docs to Langchain friendly format
            #     """

            #     values_to_metadata = dict()
            #     json_doc = json.loads(json_util.dumps(document))

            #     for key, value in json_doc.items():
            #         if key == "textContent":
            #             page_content = value
            #         else:
            #             values_to_metadata[key] = value
            #     return Document(
            #         page_content=page_content, metadata=values_to_metadata
            #     )

            # tasks = [process_document(document) for document in result]
            # result = await asyncio.gather(*tasks)

            return result

        except Exception as e:
            # Make sure we log the error
            error = f"Error in vector retrieval: {type(e).__name__}: {str(e)}"

            # Properly handle error notification to run_manager if it exists
            # but wrap it in another try/except to handle tracing errors
            if run_manager:
                try:
                    await run_manager.on_retriever_error(e)
                except Exception as trace_error:
                    error = (
                        "Warning: Error in run_manager callback: "
                        f"{str(trace_error)}"
                    )
                    # Don't let callback errors stop us from routing to MongoDB

            # Re-raise the error so it can be caught by retrieve_VI
            raise
