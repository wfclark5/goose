import duckdb
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS


def create_server(db_path: str) -> FastMCP:
    mcp = FastMCP("duckdb")

    @mcp.tool()
    def query(sql: str) -> list:
        """Execute a SQL query using DuckDB and return the results."""
        try:
            conn = duckdb.connect(database=db_path)
            res = conn.execute(sql).fetchall()
            conn.close()
            return res
        except duckdb.Error as e:
            raise McpError(ErrorData(INVALID_PARAMS, str(e))) from e
        except Exception as e:  # noqa: BLE001
            raise McpError(ErrorData(INTERNAL_ERROR, f"Unexpected error: {e}")) from e

    return mcp
