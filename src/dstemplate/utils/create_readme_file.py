from pathlib import Path

def create_readme_file(root="."):
    file = Path(root) / "README.md"
    file.touch(exist_ok=True)