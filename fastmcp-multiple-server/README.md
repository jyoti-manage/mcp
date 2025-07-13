No need to keep running the server.

Server Composition:

1. Importing
    - One time copy (static): copies all components (tools, resources, templates, prompts) from one FastMCP instance (the subserver) into another (the main server)
    - Changes to subserver NOT reflected: Note that import_server performs a one-time copy of components. Changes made to the subserver after importing will not be reflected in main_mcp. The subserver’s lifespan context is also not executed by the main server.


2. Mounting
    - Live link (dynamic): creates a live link between the main_mcp server and the subserver. Instead of copying components, requests for components matching the optional prefix are delegated to the subserver at runtime
    - Changes to subserver immediately reflected: Changes to the mounted server are immediately reflected when accessed through the parent.