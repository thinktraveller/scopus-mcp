# ScopusMCP Implementation Plan

This plan outlines the creation of a Scopus Model Context Protocol (MCP) server, allowing AI agents to query the Scopus database. The system will be modular, robust, and follow the provided documentation.

## 1. Project Structure
```text
ScopusMCP/
├── config.json              # Configuration file (API Key)
├── pyproject.toml           # Project dependencies and metadata
├── README.md                # Documentation
├── src/
│   └── scopus_mcp/
│       ├── __init__.py
│       ├── config.py        # Config loader
│       ├── client.py        # Core API client (Requests, Rate Limiting, Retries)
│       ├── cache.py         # Caching mechanism
│       ├── utils.py         # XML/JSON parsing and data cleaning
│       └── server.py        # MCP Server entry point (Tools definition)
└── tests/
    ├── __init__.py
    ├── test_client.py       # Unit tests for API client
    └── test_integration.py  # End-to-end integration tests
```

## 2. Implementation Details

### A. Configuration & Dependencies
- **Dependency Management**: Use `pyproject.toml` to define dependencies (`requests`, `mcp`, `xmltodict`).
- **Config**: `config.json` will store the provided API key (`676f8b93c67fa006c020f97e7d62752d`).

### B. Core Modules
1.  **`client.py`**:
    -   **Class**: `ScopusClient`
    -   **Authentication**: Uses `X-ELS-APIKey` header.
    -   **Rate Limiting**: Respects `X-RateLimit-*` headers and implements `time.sleep` if necessary.
    -   **Error Handling**: Catches 429 (Quota), 401 (Auth), and 5xx errors with exponential backoff retries.
    -   **Pagination**: Implements cursor-based or offset-based pagination for batch retrieval.
2.  **`cache.py`**:
    -   **Mechanism**: File-based JSON cache (hashed URL/Params as key).
    -   **Logic**: Before request, check cache -> if valid & not expired -> return cache. Else -> fetch -> save.
3.  **`utils.py`**:
    -   **Parsing**: Helpers to normalize deeply nested JSON/XML responses from Scopus into flat, usable dictionaries.

### C. MCP Server (`server.py`)
Will expose the following **Tools** to the AI:
1.  **`search_scopus`**:
    -   *Args*: `query` (str), `count` (int), `sort` (str).
    -   *Description*: Advanced search using Scopus query syntax.
2.  **`get_abstract_details`**:
    -   *Args*: `scopus_id` or `doi`.
    -   *Description*: Retrieves full abstract, authors, and metadata.
3.  **`get_author_profile`**:
    -   *Args*: `author_id`.
    -   *Description*: Retrieves author metrics, affiliation, and document count.

### D. Testing Strategy
-   **Unit Tests**: Mock `requests.get` to test error handling and parsing without hitting the real API.
-   **Integration Tests**: Test actual connectivity with the provided key (verifying the "heartbeat" of the API).

## 3. Documentation
-   **README.md**:
    -   Installation instructions.
    -   Configuration guide.
    -   List of available tools and their arguments.
    -   Examples of Scopus query syntax.

## 4. Execution Plan
1.  Create project structure and configuration files.
2.  Implement `cache.py` and `utils.py`.
3.  Implement `client.py` with robust error handling.
4.  Implement `server.py` using the `mcp` SDK.
5.  Write and run tests.
6.  Verify output format matches `uvx` / standard studio requirements.