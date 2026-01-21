#!/usr/bin/env python
from cookiecutter.main import cookiecutter
import tempfile
import os
import subprocess
import shutil

with tempfile.TemporaryDirectory() as tmpdir:
    result = cookiecutter(
        '.',
        no_input=True,
        output_dir=tmpdir,
        extra_context={
            'plugin_name': 'test-plugin',
            'include_north_tools': 'True',
            'include_normalizer': 'True',
            'include_app': 'True',
            'include_parser': 'True',
            'include_schema_package': 'True'
        }
    )
    print('Generated at:', result)

    # Copy tox.ini
    tox_plugin_path = os.path.join(result, "tox.ini")
    shutil.copy("tox.ini", tox_plugin_path)

    # Run tox
    command = [
        "tox",
        "--workdir",
        result,
        "-c",
        tox_plugin_path,
        "run",
        "-e",
        "py312"
    ]

    print(f'\nRunning: {" ".join(command)}\n')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    print("STDOUT:")
    print(stdout)
    print("\nSTDERR:")
    print(stderr)
    print(f"\nReturn code: {process.returncode}")