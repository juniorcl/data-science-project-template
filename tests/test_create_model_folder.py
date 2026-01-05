from dstemplate.utils import create_model_folder

def test_create_model_folder(project_root):
    create_model_folder(project_root)
    assert (project_root / "model").is_dir()