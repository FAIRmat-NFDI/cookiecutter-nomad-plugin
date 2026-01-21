#!/usr/bin/env python
from cookiecutter.main import cookiecutter
import tempfile
import os
import tomllib

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

    # Check generated pyproject.toml
    pyproject_path = os.path.join(result, 'pyproject.toml')
    print(f'\nChecking pyproject.toml at: {pyproject_path}')

    # Try to parse it
    try:
        with open(pyproject_path, 'rb') as f:
            config = tomllib.load(f)
        print('✓ pyproject.toml parsed successfully!')

        # Check the north_tools entry point
        if 'project' in config and 'entry-points' in config['project']:
            entry_points = config['project']['entry-points']
            if 'nomad_plugin.north_tools' in entry_points:
                print(f'  north_tool_entry_point = {entry_points["nomad_plugin.north_tools"]["north_tool_entry_point"]}')

    except Exception as e:
        print(f'✗ Failed to parse pyproject.toml: {e}')
        print('\n--- Content around the error ---')
        with open(pyproject_path, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines[160:170], 160):
                print(f'{i:3}: {line}', end='')