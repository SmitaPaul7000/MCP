import asyncio
import sys
from fastmcp import FastMCP
from router import route_query

mcp = FastMCP()

@mcp.tool()
async def routed_answer(query: str) -> str:
    resp = await route_query(query)
    return resp["answer"]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "stdio"
    if mode == "stdio":
        mcp.run()
    elif mode == "http":
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
        mcp.run_http(port=port)