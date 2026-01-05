from pathlib import Path

def create_license_file(root="."):
    file = Path(root) / "LICENSE"
    file.touch(exist_ok=True)