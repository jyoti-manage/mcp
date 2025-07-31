Langchain has created mcp-langchain adapter. 

<br/>

The Readme file of this repo is all you may need:
```
https://github.com/langchain-ai/langchain-mcp-adapters
```

<br/>

Features - \
🛠️ Convert MCP tools into LangChain tools that can be used with LangGraph agents \
📦 A client implementation that allows you to connect to multiple MCP servers and load tools from them


<br/>
<br/>


The repo for this project:
```
https://github.com/kenneth-liao/mcp-intro
```
This tutorial demonstrates how to integrate Model Context Protocol (MCP) servers with Langgraph agents to create powerful, tool-enabled AI applications. The project showcases a data science assistant named `Scout` that can help users manage their data science projects using various MCP-powered tools.



<br/>

Note: Every framework has their own way of defining tools like langchain use StructuredTool or @tool in langchain. But the MCP tools are also different in syntax. (just the syntax of all these frameworks's tools are different) (So, the mcp still solve the problem that, only one mcp tool is being created and that will be used by all the frameworks). So, for each framework, they create their own client and that client will create session with the mcp servers and get tools list and call server's tools and all of these actions are abstracted by these framework under their client. So, all the frameworks have implemented thier solution to adding MCP servers very easily. 




