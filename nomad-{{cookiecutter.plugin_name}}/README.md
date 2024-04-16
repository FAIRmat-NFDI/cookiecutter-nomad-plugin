# nomad-{{cookiecutter.plugin_name}}

{{cookiecutter.short_description}}

----

This `nomad`_ plugin was generated with `Cookiecutter`_ along with `@nomad`_'s `cookiecutter-nomad-plugin`_ template.


### Install

You should create a virtual environment. You will need the `nomad-lab` package (and `pytest`).
We recommend using Python 3.9.

```sh
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install --upgrade pip
pip install -e '.[dev]' --index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
```

**Note!**
Until we have an official pypi NOMAD release with the plugins functionality. Make
sure to include NOMAD's internal package registry (e.g. via `--index-url`).

### Testing

You can run automated tests with `pytest`:

```sh
pytest -svx tests
```

### Run linting

```sh
ruff check .
```

### Run auto-formatting

This is entirely optional. To add this as a check in github actions pipeline, uncomment the `ruff-formatting` step in `./github/workflows/actions.yaml`.

```sh
ruff format .
```

{% if cookiecutter.include_schema  -%}
You can parse an example archive that uses the schema with `nomad`
(installed via `nomad-lab` Python package):

```sh
nomad parse tests/data/test.archive.yaml --show-archive
```

### Developing your schema

You can now start to develop you schema. Here are a few things that you might want to change:

- The metadata in `nomad_plugin.yaml`.
- The name of the example section `ExampleSection`. You will also want to define more than one section.
- When you change module and class names, make sure to update the `nomad_plugin.yaml` accordingly.
{%- endif %}
{% if cookiecutter.include_parser  -%}
### Developing your parser

You can now start to develop you schema. Here are a few things that you might want to change:

- The metadata in `nomad_plugin.yaml`.
- The name of the example parser `ExampleParser` and the schema definitions it might define.
- When you change module and class names, make sure to update the `nomad_plugin.yaml` accordingly.
{%- endif %}
{% if cookiecutter.include_normalizer  -%}
### Developing your normalizer

You can now start to develop your normalizer. Here are a few things that you might want to change:

- The metadata in `nomad_plugin.yaml`.
- The name of the example section `ExampleSection`. You will also want to define more than one section.
-  The name of the example normalizer `ExampleNormalizer`. You will also want to extend the normalizer.
- When you change module and class names, make sure to update the `nomad_plugin.yaml` accordingly.
{%- endif %}

### Build the python package

The `pyproject.toml` file contains everything that is necessary to turn the project
into a pip installable python package. Run the python build tool to create a package distribution:

```
pip install build
python -m build --sdist
```

You can install the package with pip:

```
pip install dist/nomad-{{cookiecutter.plugin_name}}-{{cookiecutter.version}}
```

Read more about python packages, `pyproject.toml`, and how to upload packages to PyPI
on the [PyPI documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/).



### License
Distributed under the terms of the `{{cookiecutter.license}}`_ license, "nomad-{{cookiecutter.plugin_name}}" is free and open source software

