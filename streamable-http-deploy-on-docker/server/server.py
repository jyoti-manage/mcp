from mcp.server.fastmcp import FastMCP

# Why this happens:
# 127.0.0.1 (localhost) inside a Docker container only accepts connections from within that container
# 0.0.0.0 accepts connections from any network interface, allowing your host machine to connect through the port mapping

# host=127.0.0.1 would be binding to the localhost:8000 for just the container 
# server should be binded to 0.0.0.0:8000 inside the container, not just localhost:8000 or 127.0.0.1:8000
# It needs to bind to 0.0.0.0:8000 to be accessible from outside the container.
mcp = FastMCP("Docker-Server", host="0.0.0.0")

@mcp.tool(description="Add two numbers")
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool(description="Substract two numbers")
def sub(a: int, b: int) -> int:
    return a - b

@mcp.tool(description="Multiply two numbers")
def mul(a: int, b: int) -> int:
    return a * b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")