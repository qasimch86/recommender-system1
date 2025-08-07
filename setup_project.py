import os

# Base project directory (assumes script is in same folder or one level up)
base_dir = os.path.abspath("Recommender_system")

# Define the directory structure
folders = [
    os.path.join(base_dir, "app"),
]

files = {
    os.path.join(base_dir, "requirements.txt"): "",
    os.path.join(base_dir, "Dockerfile"): "# Dockerfile (optional)",
    os.path.join(base_dir, ".gitignore"): "venv/\n__pycache__/\n*.pyc",
    os.path.join(base_dir, "README.md"): "# Recommender System\n\nProject description goes here.",
    os.path.join(base_dir, "app", "__init__.py"): "",
    os.path.join(base_dir, "app", "main.py"): '''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Recommender System API"}
''',
    os.path.join(base_dir, "app", "database.py"): "# Database connection logic goes here\n",
    os.path.join(base_dir, "app", "recommender.py"): "# Recommender system logic goes here\n",
    os.path.join(base_dir, "app", "models.py"): "# SQLAlchemy models (if any)\n",
    os.path.join(base_dir, "app", "utils.py"): "# Helper functions\n"
}

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Project structure created successfully!")
