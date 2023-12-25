import pathlib

cookies = ["core", "django"]

# get all files within _common
common_files = pathlib.Path("_common").glob("*")
for file in common_files:
    for cookie in cookies:
        new = pathlib.Path(cookie) / "{{cookiecutter.project_slug}}" / file.name
        new.unlink(missing_ok=True)
        new.symlink_to(".." / file)
