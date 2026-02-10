# {{cookiecutter.north_tool_name}} - NORTH tool

This directory contains the configuration and a minimal Dockerfile template for defining a NORTH (NOMAD Remote Tools Hub) tool.

## Quick start

The {{cookiecutter.north_tool_name}} NORTH tool provides a containerized environment e.g., Jupyter notebook for interactive analysis with the {{cookiecutter.plugin_name}} plugin.

## Base Image

This tool uses a pre-built base image that includes the NOMAD NORTH environment. You can choose between two base images:

1. **nomad-north-jupyter** — JupyterLab-based environment
   - Repository: https://github.com/FAIRmat-NFDI/nomad-north-jupyter
   - Image: `ghcr.io/fairmat-nfdi/nomad-north-jupyter:main`

2. **nomad-north-desktop-base** — Desktop-based environment
   - Repository: https://github.com/FAIRmat-NFDI/nomad-north-desktop-base
   - Image: `ghcr.io/fairmat-nfdi/nomad-north-desktop-base:main`

Select the appropriate base image for your use case. The {{cookiecutter.plugin_name}} plugin can be installed on top of your chosen base image during the Docker build process (for this you need to extend the Dockerfile).


## Building and testing

Build the Docker image locally:

```bash
docker build -f src/{{cookiecutter.module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile \
    -t ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}:latest .
```

Test the image (for jupyter notebook image):

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
