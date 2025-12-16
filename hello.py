from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("hello-mcp")

@mcp.tool()
def add(a:int|float, b:int|float) -> int|float:
    return a-b

@mcp.tool()
def subtraction(a:int|float, b:int|float) -> int|float:
    return a-b

@mcp.tool()
def division(a:int|float, b:int|float) -> int|float:
    return a/b

@mcp.tool()
def multiplication(a:int|float, b:int|float) -> int|float:
    return a*b

if __name__ == "__main__":
    mcp.run(transport="stdio")