# DuckDB MCP Server

This example shows how to expose a [DuckDB](https://duckdb.org) database through the Model Context Protocol (MCP). It provides a simple `query` tool that executes SQL against a DuckDB database file and returns the results.

## Running with MCP Inspector

1. Install dependencies in a virtual environment:
   ```bash
   uv sync
   ```
2. Activate your environment:
   ```bash
   source .venv/bin/activate
   ```
3. Start the server in development mode:
   ```bash
   mcp dev src/duckdb_mcp/server.py
   ```
4. Open `http://localhost:5173` to access the MCP Inspector and test the `query` tool.

## Using the CLI

Install the project locally and invoke the CLI binary:

```bash
uv pip install .
duckdb-mcp --help
```
