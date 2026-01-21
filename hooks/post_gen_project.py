#!/usr/bin/env python

import logging
import os
import shutil
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("post_gen_project")

ALL_TEMP_FOLDERS = ["licenses", "py_sources"]

PY_SOURCES = "py_sources"


def move_py_files(variant, save_path, save_type):
    if variant == "none" or save_path == "none":
        return

    logger.info("Initializing python for %s - %s", variant, save_type)

    py_files = glob.glob(f"{PY_SOURCES}/{save_type}/{variant}/*")

    for src_path in py_files:
        filename = os.path.basename(src_path)
        dst_path = os.path.join(save_path, filename)

        logger.info("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_redundant_init_files(root, variant, file_type):
    if variant == "none" or file_type == "none":
        return
    source_pattern = f"{root}"
    if file_type:
        source_pattern += f"/{file_type}"
    source_pattern += f"/{variant}"
    if os.path.isdir(source_pattern):
        source_pattern += "/*"

    logger.info("Removing redundant files for %s in %s.", variant, file_type)

    files = glob.glob(source_pattern)
    logger.info("Found Redundant files: %s", files)
    for f in files:
        logger.info("Removing redundant file %s.", f)
        os.remove(f)


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.info("Remove temporary folder: %s", folder)
        shutil.rmtree(folder)


if __name__ == "__main__":
    root = os.getcwd()
    variants = [
        variant
        for variant, condition in [
            ("north_tools", "{{cookiecutter.include_north_tools}}"),
            ("schema_packages", "{{cookiecutter.include_schema_package}}"),
            ("normalizers", "{{cookiecutter.include_normalizer}}"),
            ("parsers", "{{cookiecutter.include_parser}}"),
            ("apps", "{{cookiecutter.include_app}}"),
            ("example_uploads", "{{cookiecutter.include_example_uploads}}"),
            ("actions", "{{cookiecutter.include_action}}"),
        ]
        if condition != "False"
    ]
    module_name = "{{cookiecutter.module_name}}"
    src_path = os.path.join(root, "src", module_name)
    assert os.path.isdir(src_path), f"{src_path=} doesn't exist"
    test_path = os.path.join(root, "tests")
    assert os.path.isdir(test_path), f"{test_path=} doesn't exist"
    test_data_path = os.path.join(test_path, "data")
    assert os.path.isdir(test_data_path), f"{test_data_path=} doesn't exist"
    for variant in variants:
        src_save_path = os.path.join(src_path, variant)
        os.makedirs(src_save_path, exist_ok=True)
        move_py_files(variant=variant, save_path=src_save_path, save_type="src")
        test_save_path = os.path.join(test_path, variant)
        os.makedirs(test_save_path, exist_ok=True)
        move_py_files(variant=variant, save_path=test_save_path, save_type="tests")
        if variant != "apps" and variant != "example_uploads":
            # apps and example upoads don't have tests data
            move_py_files(
                variant=variant, save_path=test_data_path, save_type="tests_data"
            )
    # Remove redundant init files
    if "north_tools" not in variants:
        remove_redundant_init_files(
            root=root, variant="publish_north.yml", file_type=".github/workflows"
        )
        remove_redundant_init_files(root=root, variant=".dockerignore", file_type="")
    remove_temp_folders(ALL_TEMP_FOLDERS)
