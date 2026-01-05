from pathlib import Path

def create_model_folder(root="."):
    folder = Path(root) / "model"
    folder.mkdir(parents=True, exist_ok=True)