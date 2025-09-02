from agents import risk_agent, ras_agent, icap_agent

async def route_query(query: str):
    q = query.lower()
    if any(k in q for k in ["risk id", "riskid", "risk"]):
        return await risk_agent.ainvoke({"query": query})
    if any(k in q for k in ["ras", "regulatory"]):
        return await ras_agent.ainvoke({"query": query})
    if any(k in q for k in ["icap", "capital"]):
        return await icap_agent.ainvoke({"query": query})
    return {"answer": "I'm sorry, I can only answer about RISK, RAS, or ICAP."}
