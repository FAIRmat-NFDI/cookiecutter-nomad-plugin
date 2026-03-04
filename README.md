# cookiecutter-nomad-plugin

Minimal [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for authoring [nomad] plugins.

## Getting started

Install [Cruft](https://github.com/cruft/cruft) and generate a new nomad plugin project:

```no-highlight
# pipx is strongly recommended.
pipx install cruft

# If pipx is not an option,
# you can install cruft in your Python user directory.
python -m pip install --user cruft
$ cruft create https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin
```

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [John Doe]: Citizen Kane
email [john.doe@physik.hu-berlin.de]: citizen@kane.de
github_username [Github organization or profile name, default: foo]: kane
plugin_name [foobar]: nomad-awesome-tools
module_name [nomad_awesome_tools]: nomad_awesome_tools
short_description [NOMAD example template]: An awesome plugin for NOMAD
version [0.1.0]:
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0+
Choose from 1, 2, 3 [1]: 2
include_schema_package [y/n] (y): y
include_normalizer [y/n] (y): n
include_parser [y/n] (y): y
include_app [y/n] (y): n
include_example_uploads [y/n] (y): n
Include NOMAD Actions (NEW in nomad-lab v1.4+) [y/n] (y): y
Include NOMAD North Tools (NEW in nomad-lab v1.4+) [y/n] (n): y
Name of the NORTH tool to be displayed in the list of NOMAD NORTH tools. For include_north_tools == n, this will be ignored. (my_north_tool):

INFO:post_gen_project:Initializing python for package - src
..
INFO:post_gen_project:Remove temporary folder: licenses
INFO:post_gen_project:Remove temporary folder: macros
INFO:post_gen_project:Remove temporary folder: py_sources
```

There you go - you just created a minimal nomad plugin:

```no-highlight
├── nomad-awesome-tools/
│   ├── LICENSE
│   ├── MANIFEST.in
│   ├── pyproject.toml
│   ├── README.md
│   ├── src/
│   │   ├── nomad_awesome_tools/
│   │   │   ├── actions/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── simple_action/
│   │   │   │   │   ├── activities.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── models.py
│   │   │   │   │   ├── workflows.py
│   │   │   ├── __init__.py
│   │   │   ├── north_tools/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── my_north_tool/
│   │   │   │   │   ├── Dockerfile
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── README.md
│   │   │   ├── parsers/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── parser.py
│   │   │   ├── schema_packages/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── schema_package.py
│   ├── tests/
│   │   ├── actions/
│   │   │   ├── test_action.py
│   │   ├── conftest.py
│   │   ├── data/
│   │   │   ├── example.out
│   │   │   ├── test.archive.yaml
│   │   ├── north_tools/
│   │   │   ├── test_north_tools.py
│   │   ├── parsers/
│   │   │   ├── test_parser.py
│   │   ├── schema_packages/
│   │   │   ├── test_schema_package.py
```


## Features

- Installable [PyPI](https://pypi.org/) package featuring a `pyproject.toml`.
- Working example code
- Comprehensive `README.md` file that contains useful information about your
  plugin
- Continuous integration configuration for [GitHub Actions](https://github.com/features/actions)
- Optional documentation with [MkDocs](https://github.com/mkdocs/mkdocs)
- Choose from several licenses, such as [MIT], [BSD-3], [Apache v2.0], [GNU GPL
  v3.0+], or [MPL v2.0]

## Issues

If you encounter any problems, please [file an issue](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin/issues/new) along with a
detailed description.

## License

Distributed under the terms of the [MIT license](./LICENSE), Cookiecutter nomad
Plugin is free and open source software.

This template is a forked version of the [`cookiecutter-pytest-plugin`](https://github.com/pytest-dev/cookiecutter-pytest-plugin). Special thanks to the contributors of the pytest cookiecutter template.
