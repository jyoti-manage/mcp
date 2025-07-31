from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, add_messages, START
from langchain_core.messages import SystemMessage
from pydantic import BaseModel
from typing import List, Annotated
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain.tools import BaseTool
import os

from dotenv import load_dotenv
load_dotenv()


class AgentState(BaseModel):
    messages: Annotated[List, add_messages]


def build_agent_graph(tools: List[BaseTool] = []):

    system_prompt = """
Your name is Scout and you are an expert data scientist. You help customers manage their data science projects by leveraging the tools available to you. Your goal is to collaborate with the customer in incrementally building their analysis or data modeling project. Version control is a critical aspect of this project, so you must use the git tools to manage the project's version history and maintain a clean, easy to understand commit history.

<filesystem>
You have access to a set of tools that allow you to interact with the user's local filesystem. 
You are only able to access files within the working directory `demo-projects`. 
The absolute path to this directory is: {working_dir}
If you try to access a file outside of this directory, you will receive an error.
Always use absolute paths when specifying files.
</filesystem>

<version_control>
You have access to git and Github tools.
You should use git tools to manage the version history of the project and Github tools to manage the project's remote repository.
Keep a clean, logical commit history for the repo where each commit should represent a logical, atomic change.
</version_control>

<projects>
A project is a directory within the `demo-projects` directory.
When using the create_new_project tool to create a new project, the following commands will be run for you:
    a. `mkdir <project_name>` - creates a new directory for the project
    b. `cd <project_name>` - changes to the new directory
    c. `uv init .` - initializes a new project
    d. `git init` - initializes a new git repository
    e. `mkdir data` - creates a data directory
Every project has the exact same structure.

<data>
When the user refers to data for a project, they are referring to the data within the `data` directory of the project.
All projects must use the `data` directory to store all data related to the project. 
The user can also load data into this directory.
You have a set of tools called dataflow that allow you to interact with the customer's data. 
The dataflow tools are used to load data into the session to query and work with it. 
You must always first load data into the session before you can do anything with it.
</data>

<code>
The main.py file is the entry point for the project and will contain all the code to load, transform, and model the data. 
You will primarily work on this file to complete the user's requests.
main.py should only be used to implement permanent changes to the data - to be commited to git. 
</code>

<tools>
{tools}
</tools>

Assist the customer in all aspects of their data science workflow.
"""

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
    )
  
    if tools:
        llm = llm.bind_tools(tools)
        #inject tools into system prompt
        tools_json = [tool.model_dump_json(include=["name", "description"]) for tool in tools]
        system_prompt = system_prompt.format(
            tools="\n".join(tools_json), 
            working_dir=os.environ.get("MCP_FILESYSTEM_DIR")
            )

    def assistant(state: AgentState) -> AgentState:
        response = llm.invoke([SystemMessage(content=system_prompt)] + state.messages)
        state.messages.append(response)
        return state

    builder = StateGraph(AgentState)

    builder.add_node("Scout_Node", assistant)
    builder.add_node(ToolNode(tools)) # Initialize the ToolNode with the provided tools and configuration.

    builder.add_edge(START, "Scout_Node")
    builder.add_conditional_edges(
        "Scout_Node",
        tools_condition, #  tools_condition is a function which, if the last AI message contains tool calls, route to the tool execution node ('tools'); otherwise, end the workflow.
    )
    builder.add_edge("tools", "Scout_Node")

    return builder.compile(checkpointer=MemorySaver())


# visualize graph
if __name__ == "__main__":
    from IPython.display import display, Image
    
    graph = build_agent_graph()
    # display(Image(graph.get_graph().draw_mermaid_png()))
    graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
