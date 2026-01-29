# {{cookiecutter.north_tool_name}} - NORTH Jupyter tool

This directory contains the NORTH tool configuration and Docker image for a Jupyter-based tool in the NOMAD NORTH (NOMAD Oasis Remote Tools Hub) environment.

## Quick start

The {{cookiecutter.north_tool_name}} NORTH tool provides a containerized JupyterLab environment for interactive analysis with the {{cookiecutter.plugin_name}} plugin.

## Building and testing

Build the Docker image locally:

```bash
docker build -f src/{{cookiecutter.module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile \
    -t ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}:latest .
```

Test the image:

```bash
docker run -p 8888:8888 ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive documentation on creating and managing NORTH tools, including detailed about some of the topic e.g.,

- Entry point configuration and `NORTHTool` API
- Docker image structure and best practices
- Dependency management

See the [NOMAD NORTH Tools documentation](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html).

