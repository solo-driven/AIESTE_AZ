# AIESTE AZERBAIJAN

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/solo-driven/AIESTE_AZ.git
    ```

2. Navigate to the project directory:
    ```bash
    cd AIESTE_AZ
    ```

3. Create a virtual environment:
    ```bash
    python3.11 -m venv env
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source env/bin/activate
        ```

5. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Navigate to the `api` directory:
    ```bash
    cd api
    ```

2. Run the application:
    ```bash
    uvicorn posts.web.main:app
    ```

Now, you can visit `http://localhost:8000/docs` in your browser to view and test the api.

