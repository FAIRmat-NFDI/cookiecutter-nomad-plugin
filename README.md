# cookiecutter-nomad-plugin

Minimal [Cookiecutter] template for authoring [nomad] plugins.

## Getting Started

Install [Cruf] and generate a new nomad plugin project:

```no-highlight
# pipx is strongly recommended.
pipx install cruft

# If pipx is not an option,
# you can install cruft in your Python user directory.
python -m pip install --user cruft
$ cruft create https://github.com/blueraft/cookiecutter-nomad-plugin
```

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [John Doe]: Citizen Kane
email [john.doe@physik.hu-berlin.de]: citizen@kane.de
github_username [foo]: kane
plugin_name [foobar]: awesome
module_name [awesome]: awesome
short_description [Nomad example template]: An awesome plugin for nomad
version [0.1.0]:
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0+
Choose from 1, 2, 3 [1]: 2
Select variant:
1 - schema
2 - normalizer
3 - parser
Choose from 1, 2, 3 [1]: 2

INFO:post_gen_project:Initializing python for schema - src
..
INFO:post_gen_project:Remove temporary folder: licenses
INFO:post_gen_project:Remove temporary folder: macros
INFO:post_gen_project:Remove temporary folder: py_sources
```

There you go - you just created a minimal nomad plugin:

```no-highlight
nomad-awesome/
├── LICENSE
├── README.rst
├── pyproject.toml
├── src
│   └── noamd_awesome
│       ├── __init__.py
│       └── plugin.py
├── tests
│   ├── conftest.py
│   └── test_awesome.py
└── MANIFEST.in
```


## Features

- Installable [PyPI] package featuring a `pyproject.toml`.
- Working example code 
- Comprehensive `README.rst` file that contains useful information about your
  plugin
- Continuous integration configuration for [GitHub Actions]
- Optional documentation with [MkDocs]
- Choose from several licenses, such as [MIT], [BSD-3], [Apache v2.0], [GNU GPL
  v3.0+], or [MPL v2.0]

## Issues

If you encounter any problems, please [file an issue] along with a
detailed description.

## License

Distributed under the terms of the [MIT license], Cookiecutter nomad
Plugin is free and open source software.
