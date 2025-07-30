from gamer.utils.prompts.code_query_router import get_code_query_prompt
from gamer.utils.models import(
    code_query_route_agent
)

def set_query(state: dict):
    query = state["messages"][-1].content
    tool_call_count = 0
    return {
        "query": query,
        "mongodb_call_count": tool_call_count,
        "schema_call_count": tool_call_count
    }

async def code_query_assignment(state:dict):
    query = state['query']
    code_query_prompt = get_code_query_prompt(query=query)
    answer = await code_query_route_agent.ainvoke(
        code_query_prompt
    )
    route = answer['route']
    return {"code_or_query": route}  

def code_query_router(state):
    route = state["code_or_query"]

    if route == "mongodb_query":
        return "mongodb"
    # Otherwise if there is, we continue
    else:
        return "python"
    
