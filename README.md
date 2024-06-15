# Information Retrival 2024

## Running the application

1. Clone this repo:

    ```bash
    git clone https://github.com/actuallylost/inf-retrieval-2024.git
    ```

2. Create a `Python Virtual environment (venv)` in the root of the project:

    ```bash
    python -m venv <ROOT_OF_PROJECT>
    ```

3. Activate environment:

    ```bash
    # Linux/MacOS
    $ source <ROOT_OF_PROJECT>/.venv/bin/activate
    ```

    ```bash
    # Windows PowerShell
    PS <ROOT_OF_PROJECT>\.venv\Scripts\activate.ps1
    ```

4. Install necessary libraries:

    ```bash
    pip install -r requirements.txt
    ```

5. Run app using `Streamlit`:

    ```bash
    streamlit run <ROOT_OF_PROJECT>/src/Main.py 
    ```
