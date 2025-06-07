import argparse
import os
from .server import create_server


def main() -> None:
    """DuckDB MCP server entry point."""
    parser = argparse.ArgumentParser(description="Expose DuckDB queries via MCP.")
    parser.add_argument(
        "--database",
        default=os.environ.get("DUCKDB_PATH", ":memory:"),
        help="Path to DuckDB database file (default: in-memory)",
    )
    args = parser.parse_args()

    mcp = create_server(args.database)
    mcp.run()


if __name__ == "__main__":
    main()
