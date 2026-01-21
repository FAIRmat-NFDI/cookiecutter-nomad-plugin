#!/usr/bin/env python
from cookiecutter.main import cookiecutter
import tempfile
import os
import subprocess

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

    init_file = os.path.join(result, 'src/test_plugin/north_tools/test_plugin_jupyter/__init__.py')

    # Run ruff format --diff to see what it wants to change
    cmd = ['ruff', 'format', '--diff', init_file]
    result_output = subprocess.run(cmd, capture_output=True, text=True)

    print("Ruff format diff:")
    print(result_output.stdout)

    if result_output.returncode != 0:
        print(f"\nReturn code: {result_output.returncode}")
    else:
        print("\nNo formatting changes needed!")