# Scopus MCP Server

[中文](README_CN.md) | [English](README.md)

This is a Model Context Protocol (MCP) server that provides access to the Elsevier Scopus API. It allows AI assistants to search for academic papers, retrieve abstracts, and look up author profiles.

## Configuration

### Setup Steps
1.  Go to [Elsevier Developer Portal](https://dev.elsevier.com/) to apply for an API key.
2.  Fill the key into `config.json` in the project folder.
3.  Edit `MCP_tool_config.json`, modifying the folder path (pay attention to the slash direction).
4.  Finally, import the configuration into your MCP client (e.g., Claude Desktop) by copying the content of `MCP_tool_config.json`.

## 🚀 Quick Start (Zero Setup)

If you use Claude Desktop, you can skip downloading the code and just configure it directly:

1.  **Get Key**: Get a free API Key from [Elsevier Developer Portal](https://dev.elsevier.com/).
2.  **Configure**: Edit `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS).
3.  **Add**:

```json
{
  "mcpServers": {
    "scopus-assistant": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/qwe4559999/scopus-mcp.git",
        "scopus-mcp"
      ],
      "env": {
        "SCOPUS_API_KEY": "PUT_YOUR_KEY_HERE"
      }
    }
  }
}
```

*(Requires [uv](https://docs.astral.sh/uv/) installed)*

## Installation

1.  Ensure you have Python 3.10+ installed.
2.  Install dependencies:
    ```bash
    pip install .
    ```

## Usage

### Running the Server

You can run the server using `uvx` (recommended) or directly with python.

```bash
# Using uvx
uvx --from . scopus-mcp

# Or directly
python -m scopus_mcp.server
```

### Available Tools

1.  **`search_scopus`**
    -   Searches the Scopus database using the standard query syntax.
    -   Arguments:
        -   `query` (string): The search query (e.g., `TITLE("Artificial Intelligence")`).
        -   `count` (integer): Number of results to return (default: 5).
        -   `sort` (string): Sort order (e.g., `coverDate`).

2.  **`get_abstract_details`**
    -   Retrieves detailed information for a specific document.
    -   Arguments:
        -   `scopus_id` (string): The Scopus ID of the document.

3.  **`get_author_profile`**
    -   Retrieves an author's profile information.
    -   Arguments:
        -   `author_id` (string): The Scopus Author ID.

## Development

Run tests with:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments & Contributors

*   **[thinktraveller](https://github.com/thinktraveller)** - *Initial Work & Core Development*
*   **[qwe4559999](https://github.com/qwe4559999)** - *Maintainer*
