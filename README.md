# Example local MLflow server setup within a VS Code Dev Container

This repository provides a minimal example for running a local MLflow server inside a VS Code Dev Container.
It includes:

- A Python development environment, specified in [Dockerfile](Dockerfile).
- A standalone MLflow server with a local SQLite database backend and local artifact store.

This multi-container application is orchestrated using Docker Compose.

## Usage

1. Install and launch [Docker](https://www.docker.com/).
2. Install and open the project in VS Code.
3. Open the container by using the command palette in VS Code (`Ctrl + Shift + P`) to search for "Dev Containers: Open Folder in Container...".

The MLflow UI is accessible at [http://localhost:5000](http://localhost:5000).

To verify the integration, execute the test script with:

```bash
python ./test-mlflow.py
```

## 🗂️ File structure

```text
.
├── .devcontainer/             # VS Code Dev Container setup
│   ├── devcontainer.json      # Dev Container configuration
│   └── docker-compose.yml     # Multi-container orchestration
├── mlflow/                    # MLflow local storage (git ignored)
│   ├── artifacts/             # Artifact store
│   └── db/                    # Database
├── Dockerfile                 # Dockerfile defining the Python environment
├── requirements.in            # Direct dependencies for the Python application
├── requirements.txt           # Pinned dependencies (generated)
├── test-mlflow.py             # Script to test the MLflow integration
```
