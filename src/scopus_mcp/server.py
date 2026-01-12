import asyncio
import logging
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from .client import ScopusClient
from .utils import clean_search_results, clean_abstract_details, clean_author_profile

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scopus-mcp")

# Initialize Server
server = Server("scopus-mcp")
client = ScopusClient()

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search_scopus",
            description="Search for documents in Scopus using a query string.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The Scopus search query (e.g., 'TITLE(AI) AND PUBYEAR > 2020')."
                    },
                    "count": {
                        "type": "integer",
                        "description": "Number of results to return (default 5, max 25).",
                        "default": 5,
                        "maximum": 25
                    },
                    "sort": {
                        "type": "string",
                        "description": "Sort order (e.g., 'coverDate', 'relevancy').",
                        "default": "coverDate"
                    }
                },
                "required": ["query"]
            }
        ),
        types.Tool(
            name="get_abstract_details",
            description="Retrieve full details for a specific document by Scopus ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "scopus_id": {
                        "type": "string",
                        "description": "The Scopus ID of the document."
                    }
                },
                "required": ["scopus_id"]
            }
        ),
        types.Tool(
            name="get_author_profile",
            description="Retrieve an author's profile by Author ID.",
            inputSchema={
                "type": "object",
                "properties": {
                    "author_id": {
                        "type": "string",
                        "description": "The Scopus Author ID."
                    }
                },
                "required": ["author_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, Any] | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if not arguments:
        arguments = {}

    try:
        if name == "search_scopus":
            query = arguments.get("query")
            count = arguments.get("count", 5)
            sort = arguments.get("sort", "coverDate")
            
            if not query:
                raise ValueError("Query is required")

            # Await the async client method
            raw_data = await client.search_scopus(query, count=count, sort=sort)
            results = clean_search_results(raw_data)
            
            return [types.TextContent(type="text", text=str(results))]

        elif name == "get_abstract_details":
            scopus_id = arguments.get("scopus_id")
            if not scopus_id:
                raise ValueError("scopus_id is required")
                
            raw_data = await client.get_abstract(scopus_id)
            details = clean_abstract_details(raw_data)
            
            return [types.TextContent(type="text", text=str(details))]

        elif name == "get_author_profile":
            author_id = arguments.get("author_id")
            if not author_id:
                raise ValueError("author_id is required")
                
            raw_data = await client.get_author(author_id)
            profile = clean_author_profile(raw_data)
            
            return [types.TextContent(type="text", text=str(profile))]

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        logger.error(f"Error executing tool {name}: {e}")
        return [types.TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    try:
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )
    finally:
        # Ensure client is closed on shutdown
        await client.close()

def start():
    """Entry point for the package script."""
    asyncio.run(main())

if __name__ == "__main__":
    start()
