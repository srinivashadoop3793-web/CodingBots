***Commands to md file to do the documentation:***
Let build our First MCP Server

mkdir hello_mcp
cd hello_mcp

Lets initialize the project
uv init .
uv sync

Activate the virtual environment
windows:  .venv\Scripts\activate

Launch vscode
code .

Add dependencies
uv add "mcp[cli]" httpx

Now lets create a file called hello.py