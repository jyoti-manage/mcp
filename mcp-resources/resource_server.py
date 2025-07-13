from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources-Server")


def read_doc(doc_name):
    # Open the file in read mode
    with open(doc_name, 'r') as file:
        # Read the contents of the file
        content = file.read()
    return content



@mcp.resource("msg:/greeting/hello")
def read_document() -> str:
    """Greeting message."""
    return "Hello! Hope you are doing well."



#  dynamic resource template
@mcp.resource("file://documents/{doc_name}")
def read_document(doc_name: str) -> str: 
    """Read a document by name."""
    file_path= f"./documents/{doc_name}"
    
    return read_doc(file_path)



if __name__ == "__main__":
    mcp.run(transport="streamable-http")