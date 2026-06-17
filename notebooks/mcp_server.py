"""
Simple MCP server for the LangGraph course.

Tools:
  - add: Add two numbers
  - multiply: Multiply two numbers
  - web_search: Search the web using SerpAPI

Run with:
  python mcp_server.py
"""

from mcp.server.fastmcp import FastMCP
from langchain_community.utilities import SerpAPIWrapper
import os

mcp = FastMCP("LangGraph Course Tools")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together. Use this for addition calculations."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers together. Use this for multiplication calculations."""
    return a * b


@mcp.tool()
def web_search(query: str) -> str:
    """Search the web for real-time information. Use this for any factual questions about current events, people, or topics."""
    try:
        serpapi = SerpAPIWrapper()
        return serpapi.run(query)
    except Exception as e:
        return f"Search error: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
