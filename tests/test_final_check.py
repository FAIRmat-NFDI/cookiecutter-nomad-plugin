#!/usr/bin/env python
"""Test to verify the cookiecutter template generates correctly with north_tools."""
from cookiecutter.main import cookiecutter
import tempfile
import os
import subprocess
import shutil

def check_file_exists(base_path, relative_path, should_exist=True):
    full_path = os.path.join(base_path, relative_path)
    exists = os.path.exists(full_path)
    status = "✓" if exists == should_exist else "✗"
    expectation = "exists" if should_exist else "doesn't exist"
    print(f"  {status} {relative_path} {expectation}: {exists}")
    return exists == should_exist

with tempfile.TemporaryDirectory() as tmpdir:
    print("Generating plugin with all features enabled...")
    result = cookiecutter(
        '.',
        no_input=True,
        output_dir=tmpdir,
        extra_context={
            'plugin_name': 'long-name-foo-bar',
            'include_north_tools': 'True',
            'include_normalizer': 'True',
            'include_app': 'True',
            'include_parser': 'True',
            'include_schema_package': 'True'
        }
    )
    print(f'Generated at: {result}\n')

    module_name = 'long_name_foo_bar'

    # Check all expected files
    print("Checking generated files:")
    all_good = True

    # Check north_tools specific files
    all_good &= check_file_exists(result, f'src/{module_name}/north_tools/{module_name}_jupyter')
    all_good &= check_file_exists(result, f'src/{module_name}/north_tools/{module_name}_jupyter/__init__.py')
    all_good &= check_file_exists(result, '.dockerignore')
    all_good &= check_file_exists(result, f'tests/north_tools/test_north_tools.py')

    # Check other required files
    all_good &= check_file_exists(result, f'src/{module_name}/apps/__init__.py')
    all_good &= check_file_exists(result, f'tests/apps/test_app.py')

    print(f"\nAll files present: {all_good}")

    # Copy tox.ini and run tox (mimicking what the test does)
    print("\nCopying tox.ini and running tox...")
    tox_plugin_path = os.path.join(result, "tox.ini")
    shutil.copy("tox.ini", tox_plugin_path)

    # Run just the format check first to see what fails
    print("\nRunning ruff format check:")
    format_cmd = ['ruff', 'format', '--check', os.path.join(result, 'src'), os.path.join(result, 'tests')]
    format_result = subprocess.run(format_cmd, capture_output=True, text=True)

    if format_result.returncode != 0:
        print(f"Format check failed with code {format_result.returncode}")
        print("STDOUT:", format_result.stdout)
        print("STDERR:", format_result.stderr)

        # Show what would be reformatted
        print("\nRunning ruff format --diff to see changes:")
        diff_cmd = ['ruff', 'format', '--diff', os.path.join(result, 'src'), os.path.join(result, 'tests')]
        diff_result = subprocess.run(diff_cmd, capture_output=True, text=True)
        print(diff_result.stdout)
    else:
        print("Format check passed!")

    # Try running the actual tox command
    print("\nRunning full tox suite...")
    command = [
        "tox",
        "--workdir",
        result,
        "-c",
        tox_plugin_path,
        "run",
        "-e",
        "format"
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    print(f"Tox format check return code: {process.returncode}")
    if process.returncode != 0:
        print("STDOUT:", stdout)
        print("STDERR:", stderr)