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

INFO:post_gen_project:Initializing python for package - src
..
INFO:post_gen_project:Remove temporary folder: licenses
INFO:post_gen_project:Remove temporary folder: macros
INFO:post_gen_project:Remove temporary folder: py_sources
```

There you go - you just created a minimal nomad plugin:

```no-highlight
nomad-awesome-tools/
├── LICENSE
├── README.md
├── pyproject.toml
├── move_template_files.sh
├── src
│   └── nomad_awesome_tools
│       ├── __init__.py
|       ├── schema_packages
│       |   ├── __init__.py
│       |   └── schema_package.py
|       └── parsers
│           ├── __init__.py
│           └── parser.py
├── tests
│   ├── conftest.py
│   └── test_awesome.py
└── MANIFEST.in
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
