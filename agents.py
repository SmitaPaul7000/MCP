
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
import asyncio
from typing import Dict
from utils import diff, stream_text
from memory import update_memory, get_last

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def risk_node(state: Dict):
    last = get_last("risk")
    new_data = "RISK report ID=123, status=OK"
    update_memory("risk", new_data)
    d = diff(last, new_data)
    return {"answer": d}

async def ras_node(state: Dict):
    last = get_last("ras")
    new_data = "RAS regulatory dataset version=5"
    update_memory("ras", new_data)
    d = diff(last, new_data)
    return {"answer": d}

async def icap_node(state: Dict):
    last = get_last("icap")
    new_data = "ICAP capital ratio=12.5%"
    update_memory("icap", new_data)
    d = diff(last, new_data)
    return {"answer": d}

# Build LangGraph graphs for each agent
def build_agent(node_fn):
    sg = StateGraph(dict)
    sg.add_node("main", node_fn)
    sg.set_entry_point("main")
    return sg.compile()

risk_agent = build_agent(risk_node)
ras_agent = build_agent(ras_node)
icap_agent = build_agent(icap_node)