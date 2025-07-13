from mcp.server.fastmcp import FastMCP
import json

from pathlib import Path

base_dir = Path(__file__).parent

mcp = FastMCP("Manager")


# def read_doc(data):
#     with open("../server/json_data/data.json", "w") as f:   # the path should be relative to client.py 🫢🫢 in stdio. And if streamable-http is used, then the path is relative to server
#         json.dump(data,f,indent=2)


def read_doc(data):
    with open(base_dir / "json_data" / "data.json", "w") as f:   # This makes the file access robust no matter where the server is run from. 
        json.dump(data, f, indent=2)
   

@mcp.tool()
def sum():
    "give adding of to numbers"
    read_doc({
        "name":"messy",
        "class": "high"
})
    return "Done"


if __name__=="__main__":
    mcp.run()

