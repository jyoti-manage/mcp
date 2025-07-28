# entry point to the server
# we want to tell the package manager that when you actually download the package, how do you actually run the MCP server.

from mcpserver.deployment import mcp

def main():
    mcp.run()

if __name__ == "__main__":
    main()