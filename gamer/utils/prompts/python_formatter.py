def get_python_format_prompt(
        python_code: str,
        python_code_response: str,
        schema_context:list,
        query: int,
        ):

    python_format_prompt = (
        f"""
    You are a Python and MongoDB expert who excels in concise and organized coding . 

    Given a user's query: {query}, create python code for the following mongodb query based on the instructions outline below. 
    Use the schema context ({schema_context}) to inform yourself of how the schema is structured, and create the appropriate MongoDB queries.

    - Note that there are filter+projection queries and aggregation pipelines. Both features are distinct. Keep this in mind as you're constructing your query.
    - Format the MongoDB query using the template below
    - Use specific identifiers from the question (subject_id, name, project_name, etc.) in your filter or aggregation pipeline

    - When constructing aggregations do not use  $year or $size. 

    Note that the session field is used for physiology based modalities like behaviour, optical physiology etc and acquisition is used for modalities like smartspim or exaspim. If unsure which field the data might exist in, consider both fields. 

    Be especially careful with time based queries. I recommend removing any external calculations on time within the aggregation pipeline beyond extracting the necessary information. Conduct the calculations after the records are fetched in python.

    When displaying MongoDB queries, use this standard format:

    ```python
    import json

    from aind_data_access_api.document_db import MetadataDbClient

    API_GATEWAY_HOST = "api.allenneuraldynamics-test.org"
    DATABASE = "metadata_vector_index"
    COLLECTION = "static_eval_data_assets_3_14"

    docdb_api_client = MetadataDbClient(
        host=API_GATEWAY_HOST,
        database=DATABASE,
        collection=COLLECTION,
    )

    # For filter queries:
    filter = {{YOUR_FILTER_CRITERIA}}
    projection = {{
        "field1": 1,
        "field2": 1,
        # include relevant fields
    }}
    records = docdb_api_client.retrieve_docdb_records(
        filter_query=filter,
        projection=projection,
    )
    print(json.dumps(records, indent=3))

    # OR for aggregation pipelines:
    agg_pipeline = [
        # your pipeline stages here
    ]
    result = docdb_api_client.aggregate_docdb_records(
        pipeline=agg_pipeline
    )
    print(json.dumps(result[:10], indent=3))  # limit output to first 10 results

    There is a possibility that you will have to correct a python script. It has been sent back to you due to an error in the answer generation.
    In that case, this is the python code you will correct : ({python_code}) and this was the error/answer received : ({python_code_response}).

    Fix the syntax/logic of the code to get the desired answer. If the python code/response is empty, continue.
    Important reminders:

    Always provide complete Python code using the AIND data access API, never just the MongoDB query alone
    When generating code, only provide the user with the information they requested. Nothing more.
    Include appropriate print statements to display results
    Ensure Python boolean values are properly capitalized (True, False)
    Add a brief explanation of what the query does after displaying the code
    Be precise with MongoDB syntax and preserve the structure of filters/pipelines
    For example, if asked about subjects with CVS N2cdG-H2B-tdTomato injections, provide a complete solution following this template.
    Do not do complex computations in a Mongodb pipeline or filter, do them in python. Try to avoid computations in mongodb if possible.

    Do not hallucinate or make up fields not present in the schema_context.
    """
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{python_format_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return  messages