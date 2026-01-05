from dstemplate.utils import create_readme_file, create_license_file

def test_create_readme_file(project_root):
    create_readme_file(project_root)
    assert (project_root / "README.md").is_file()

def test_create_license_file(project_root):
    create_license_file(project_root)
    assert (project_root / "LICENSE").is_file()