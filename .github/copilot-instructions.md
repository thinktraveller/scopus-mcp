# Copilot Instructions for Scopus MCP Server

## Project Overview
This is a **Model Context Protocol (MCP) server** providing AI assistants (like Claude) access to the Elsevier Scopus academic paper database via three tools: search, abstract retrieval, and author profiles.

## Architecture: Key Design Patterns

### Async-First Design
- **All I/O is async** using `httpx.AsyncClient` and `async/await`
- Server runs via `mcp.server.stdio_server()` over stdin/stdout (not HTTP)
- Never use blocking calls in request handlers; use `await` everywhere
- Example: `await client.search_scopus(query, count, sort)` in [server.py](../src/scopus_mcp/server.py#L80)

### Layered Architecture
```
Request Flow: Server (MCP) → ScopusClient → CacheManager → httpx → Scopus API
Response Flow: API JSON → CacheManager → utils.clean_* → TextContent → Claude
```
- **server.py**: Handles MCP protocol, tool definitions, parameter validation
- **client.py**: Async HTTP requests, rate-limiting (429 backoff), retries
- **cache.py**: File-based SHA256 hashing; 24-hour expiration; silent write failures
- **utils.py**: Raw API JSON → human-readable dicts (removes metadata nesting)
- **config.py**: API key precedence: `SCOPUS_API_KEY` env var → config.json

### Configuration Precedence (Don't Override)
```
SCOPUS_API_KEY (environment) > config.json > ValueError
```
In `config.py`: `load_dotenv()` called immediately; use `os.getenv()` to check env vars first.

## Critical Implementation Patterns

### Adding New Tools
Register in `server.py` using decorator pattern:
```python
@server.list_tools()  # Called by MCP to advertise tools
@server.call_tool()   # Called when tool is invoked
```
Tool definitions must include `inputSchema` with JSON Schema (type, properties, required).
Response must be wrapped in `types.TextContent` (not raw dict).

### API Request Pattern
Every request in `client.py` goes through `_request()` internal method:
1. Check cache (quick synchronous lookup via SHA256 hash)
2. If cache miss: send request with retry loop (max 3 attempts)
3. Handle 429 rate limits by sleeping until `X-RateLimit-Reset`
4. Save successful responses to cache with timestamp
5. Log cache hits/misses at DEBUG level

### Data Cleaning Pattern
Raw Scopus JSON is deeply nested. `utils.py` extracts essential fields:
- Removed: nested `link` arrays, metadata decorators
- Extracted: scopus_id (from identifier), cover_date, cited_by_count
- Normalized: single author vs array inconsistencies
- **Always return simplified dicts** for LLM readability

### Testing Pattern
Mock external dependencies; don't hit real API:
- Patch `get_api_key()` to return fake key
- Patch `CacheManager` to avoid disk I/O
- Use `@patch('scopus_mcp.client.ScopusClient.method_name')` to mock network calls
- Tests use `unittest` + `unittest.mock`

## Build & Run Commands

### Development Setup
```bash
# Install with dev dependencies
pip install -e ".[dev]"  # or: uv pip install -e ".[dev]"

# Run tests
pytest

# Run server (for manual testing)
python -m scopus_mcp.server
```

### Deployment
```bash
# Via uvx (recommended; auto-downloads package)
uvx --from . scopus-mcp

# Or via pip + python
python -m scopus_mcp.server
```

The server starts immediately and waits for JSON-RPC requests on stdin.

## Project-Specific Conventions

### File Organization
- **Source**: All logic in `src/scopus_mcp/` (not root)
- **Build config**: `pyproject.toml` (PEP 621 standard; not setup.py)
- **Cache**: `.cache/` directory (SHA256-named JSON files; 24h TTL)
- **Config**: `config.json` or `SCOPUS_API_KEY` env var (never hardcode)
- **Tests**: `tests/` directory; use `unittest` + mocks

### Logging
- Configured in [server.py](../src/scopus_mcp/server.py#L12) and [client.py](../src/scopus_mcp/client.py#L9)
- Level: `INFO` for normal ops, `DEBUG` for cache hits, `WARNING` for rate limits
- Logger names: `"scopus-mcp"` (server), `__name__` (other modules)

### Error Handling
- **Config errors** (missing API key): Raise `ValueError` with clear message
- **Network errors** (transient): Retry with exponential backoff
- **API errors** (4xx/5xx): `response.raise_for_status()` converts to exception
- **Cache write failures**: Silently fail (don't crash app); API will return fresh data next time

### Dependencies
- **httpx** (not requests): async native, auto-handles retries/redirects
- **mcp**: MCP protocol library; don't hand-code JSON-RPC
- **python-dotenv**: Load .env file; required for local dev (SCOPUS_API_KEY)
- **pytest** + **pytest-mock**: Testing (dev only)

## Critical Files & Their Responsibilities

| File | Purpose | Key Functions |
|------|---------|---|
| [server.py](../src/scopus_mcp/server.py) | MCP entry point & tools | `handle_list_tools`, `handle_call_tool`, `start` |
| [client.py](../src/scopus_mcp/client.py) | Scopus API client | `_request`, `search_scopus`, `get_abstract_details`, `get_author_profile` |
| [cache.py](../src/scopus_mcp/cache.py) | Response caching | `get`, `set`, `_get_cache_key` |
| [utils.py](../src/scopus_mcp/utils.py) | JSON transformation | `clean_search_results`, `clean_abstract_details`, `clean_author_profile` |
| [config.py](../src/scopus_mcp/config.py) | Config loading | `get_api_key`, `load_config_file` |

## Common Debugging Scenarios

### "API Key not found" Error
Check precedence: `SCOPUS_API_KEY` env var set? → config.json exists and has `api_key` field? → Run with `-v` flag to see which was checked.

### Rate Limit Failures
Client auto-handles 429 with exponential backoff. If still failing: API quota may be exhausted (contact Elsevier). Cache can mitigate repeated queries.

### Cache Not Working
Cache uses SHA256(url + sorted params). Different param order = different cache key. Inspect `.cache/*.json` files to verify. Set `expiration_seconds` higher if needed.

### Tests Failing Due to Mocks
Ensure patches are applied **before** imports: patch in `setUp()`, not at module level. Use `self.config_patcher.stop()` in `tearDown()`.

## Extending the Project

### Adding a New Scopus API Endpoint
1. Add async method to `ScopusClient` in [client.py](../src/scopus_mcp/client.py) (follow `_request` pattern)
2. Create corresponding `clean_*()` function in [utils.py](../src/scopus_mcp/utils.py)
3. Register new tool in [server.py](../src/scopus_mcp/server.py) using `@server.tool()` decorator
4. Add unit tests in `tests/` with mocked httpx responses

### Supporting New Data Sources
The `ScopusClient` can be extended or a new `ElsevierClient` created following the same patterns:
- Same async/await discipline
- Same `_request` → cache → clean flow
- Register tools in server.py the same way

---

**Version**: 0.1.0 | **Python**: 3.10+ | **MCP Protocol**: 1.0+
