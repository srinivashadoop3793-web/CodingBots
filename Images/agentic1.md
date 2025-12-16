***Commands to md file to do the documentation:***
### Common Markdown symbols
| Purpose | Syntax |
|------|------|
| Heading | `# Heading` |
| Bold | `**bold**` |
| Italic | `*italic*` |
| List | `- item` |
| Code | `` `code` `` |
| Code block | ``` ``` |
| Link | `[text](url)` |
| Image | `![alt](image.png)` |


***Let build our First MCP Server***

mkdir hello_mcp
cd  hello_mcp

Lets initialize the project
uv init .
uv sync

Activate the virtual environment
windows:  .venv\Scripts\activate

Launch vscode
code .

Add dependencies
uv add "mcp[cli]" httpx

uv run hello.py

**Now lets create a file called hello.py**

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp =  FastMCP("hello-mcp")

@mcp.tool()
def add(a:int|float, b:int|float) -> int|float:
    return a-b

if __name__ == "__main__":
    mcp.run(transport="stdio")

**claud configuration file**
{
  "mcpServers": {
    "hello-mcp": {
      "command": "uv",
      "args": [
        "run",
        "C:\\SrinivasMuppu\\GenerativeAI\\Practivals\\hello_mcp\\.venv\\Scripts\\python.exe",
        "C:\\SrinivasMuppu\\GenerativeAI\\Practivals\\hello_mcp\\hello.py"
      ],
      "cwd": "C:\\SrinivasMuppu\\GenerativeAI\\Practivals\\hello_mcp"      
    }
  }
}

* [Refere](https://github.com/srinivashadoop3793-web/CodingBots/blob/main/Images/agentic1.md) for  changes