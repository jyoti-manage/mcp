1. Install this server into claude desktop's config.json file:
    ```
    uv run mcp install main.py
    ```
    



2. Start MCP inspector:

    ```
    uv run mcp dev main.py
    ```




3. Using uv add:

    ``` uv init ```

    Create virtual environment and activate it:
    ``` 
    uv venv
    .venv\Scripts\activate
    ```

    To install all dependencies, including those in dependency groups, from a pyproject.toml file at once using uv:
    ```
    uv sync
    ```


    ```
    uv add flask requests

    uv run main.py
    ```

    ```
    uv pip install -e .
    ```
    
- This workflow creates a project, adds dependencies, and ensures they are locked and available for all collaborators (in pyproject.toml file).


4. Using uv pip:

    ```uv venv```

    Create environment:

    ```
    .venv\Scripts\activate
    ```

    ```
    uv pip install -r req.txt
    
    uv pip install flask

    python main.py
    ```

- This workflow installs Flask into the virtual environment without locking it, suitable for quick setups.

5. 
    ```
    streamlit run .\app.py
    ```
    - re-load on every click (if condition true when clicked on it)
    - re-import only if the file is changed