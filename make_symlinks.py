#!/usr/bin/env python

""" Helper script that copies things from _common to the cookiecutter root """

import pathlib

cookies = ["core", "django"]


def symlink_all_files(from_dir, to_dir, symlink=True):
    files = pathlib.Path(from_dir).glob("*")
    # traverse within each directory
    for file in files:
        for cookie in cookies:
            new = pathlib.Path(cookie) / to_dir / file.name
            if symlink and not new.exists():
                new.symlink_to("../.." / file)
            elif not symlink:
                # copy file
                new.write_text(file.read_text())


symlink_all_files("_common", "{{cookiecutter.project_slug}}")
pathlib.Path("core/hooks").mkdir(parents=True, exist_ok=True)
pathlib.Path("django/hooks").mkdir(parents=True, exist_ok=True)
symlink_all_files("_hooks", f"hooks", symlink=False)
