import json

from langchain_core.messages import ToolMessage

from gamer.utils.tools import schema_context_tools
from gamer.utils.models import(
    schema_context_agent
)

def should_continue_schema(state):
    messages = state["messages"]
    last_message = messages[-1]
    schema_call_count = state.get("schema_call_count", 0)

    if not last_message.tool_calls:
        return "end"
    elif schema_call_count > 3:
        return "end"
    else:
        return "continue"


async def get_schema_context_tools(state: dict):
    """
    Retrieving information from MongoDB with tools
    """

    tool_call_count = state.get("schema_call_count", 0) + 1

    tools_by_name = {tool.name: tool for tool in schema_context_tools}

    outputs = []

    for i, tool_call in enumerate(state["messages"][-1].tool_calls):

        tool_result = await tools_by_name[tool_call["name"]].ainvoke(
            tool_call["args"]
        )
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )

    return {
        "messages": outputs,
        "schema_context": outputs,
        "schema_call_count": tool_call_count
    }

async def get_schema_context(state: dict):

    query = state.get("query", "No query was provided")
    schema_context= state.get("schema_context", [])
    tool_call_count = state.get("schema_call_count", 0)

    response = await schema_context_agent.ainvoke(
        {"query": query,
         "schema_context": schema_context,
         "tool_call_count": tool_call_count}
    )
    
    schema_context.append(response.content)

    return {"messages":[response],
            "schema_context": schema_context}
