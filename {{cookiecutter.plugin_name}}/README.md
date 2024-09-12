# {{cookiecutter.plugin_name}}

{{cookiecutter.short_description}}

This `nomad` plugin was generated with `Cookiecutter` along with `@nomad`'s [`cookiecutter-nomad-plugin`](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin) template.

## Development

If you want to locally develop this plugin, clone the project.

```sh
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}.git
cd {{cookiecutter.plugin_name}}
```

We highly recommend using `uv` to manage the project. Consider installing `uv` by following the official installation [guide](https://docs.astral.sh/uv/getting-started/installation/#installing-uv).

Read the short [guide](https://docs.astral.sh/uv/guides/projects/) on how to manage projects.

Install all the dependencies:

```sh
uv sync --extra-all
```

**Note!**
If you're not using `uv`, setup a `venv` and pip install the package using `pip install -e '.[dev]' --index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple`.
Until we have an official pypi NOMAD release with the plugins functionality make sure to include NOMAD's internal package registry (via --extra-index-url in the above command).

### Run the tests

You can run the tests using:

```sh
uv run pytest
```

Or generate a test coverage report:

```sh
uv run pytest --cov
```

### Run linting and auto-formatting

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting the code. Ruff auto-formatting is also a part of the GitHub workflow actions. You can check linting and formatting using:

```sh
uv run ruff check .
uv run ruff format . --check
```

### Debugging

For interactive debugging of the tests, use `pytest` with the `--pdb` flag. We recommend using an IDE for debugging, e.g., _VSCode_. If that is the case, add the following snippet to your `.vscode/launch.json`:

```json
{
  "configurations": [
    {
      "name": "<descriptive tag>",
      "type": "debugpy",
      "request": "launch",
      "cwd": "${workspaceFolder}",
      "program": "${workspaceFolder}/.venv/bin/pytest",
      "justMyCode": true,
      "env": {
        "_PYTEST_RAISE": "1"
      },
      "args": ["-sv", "--pdb", "<path-to-plugin-tests>"]
    }
  ]
}
```

where `<path-to-plugin-tests>` must be changed to the local path to the test module to be debugged.

The settings configuration file `.vscode/settings.json` automatically applies the linting and formatting upon saving the modified file.

### Documentation on Github pages

To view the documentation locally, run the docs server:

```sh
uv run mkdocs serve
```

## Adding this plugin to NOMAD

Currently, NOMAD has two distinct flavors that are relevant depending on your role as an user:

1. [A NOMAD Oasis](#adding-this-plugin-in-your-nomad-oasis): any user with a NOMAD Oasis instance.
2. [Local NOMAD installation and the source code of NOMAD](#adding-this-plugin-in-your-local-nomad-installation-and-the-source-code-of-nomad): internal developers.

### Adding this plugin in your NOMAD Oasis

Read the [NOMAD plugin documentation](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html) for all details on how to deploy the plugin on your NOMAD instance.

### Adding this plugin in your local NOMAD installation and the source code of NOMAD

Modify the text file under `/nomad/default_plugins.txt` and add:

```sh
<other-content-in-default_plugins.txt>
{{cookiecutter.plugin_name}}==x.y.z
```

where `x.y.z` represents the released version of this plugin.

Then, go to your NOMAD folder, activate your NOMAD virtual environment and run:

```sh
deactivate
cd <route-to-NOMAD-folder>/nomad
source .pyenv/bin/activate
./scripts/setup_dev_env.sh
```

Alternatively and only valid for your local NOMAD installation, you can modify `nomad.yaml` to include this plugin, see [NOMAD Oasis - Install plugins](https://nomad-lab.eu/prod/v1/staging/docs/howto/oasis/plugins_install.html).

### Build the python package

The `pyproject.toml` file contains everything that is necessary to turn the project
into a pip installable python package. Run the python build tool to create a package distribution:

```sh
uv build
```

You can install the package with pip:

```sh
pip install dist/{{cookiecutter.plugin_name}}-{{cookiecutter.version}}
```

Read more about python packages, `pyproject.toml`, and how to upload packages to PyPI
on the [PyPI documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

### Template update

We use cruft to update the project based on template changes. A `cruft-update.yml` is included in Github workflows to automatically check for updates and create pull requests to apply updates. Follow the [instructions](https://github.blog/changelog/2022-05-03-github-actions-prevent-github-actions-from-creating-and-approving-pull-requests/) on how to enable Github Actions to create pull requests.

To check for updates locally, run:

```sh
uvx cruft update
```

**Note!**
`uvx` is included in `uv` installation.

## Main contributors

| Name                       | E-mail                                                  |
| -------------------------- | ------------------------------------------------------- |
| {{cookiecutter.full_name}} | [{{cookiecutter.email}}](mailto:{{cookiecutter.email}}) |
