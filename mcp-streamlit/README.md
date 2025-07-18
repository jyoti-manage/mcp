uv run mcp install main.py
- install this server into claude config


- Using uv add:
uv init 
# Create virtual environment and activate it
uv venv
.venv\Scripts\activate
uv add flask requests
uv run main.py
- This workflow creates a project, adds dependencies, and ensures they are locked and available for all collaborators.

- Using uv pip:
uv venv
- create environment
.venv\Scripts\activate
uv pip install flask
python main.py
- This workflow installs Flask into the virtual environment without locking it, suitable for quick setups.

streamlit run .\app.py
re-load on every click (if condition true when clicked on it)
re-import only if the file is changed