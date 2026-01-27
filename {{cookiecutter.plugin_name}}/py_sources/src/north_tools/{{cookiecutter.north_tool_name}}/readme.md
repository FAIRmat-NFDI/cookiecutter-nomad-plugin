# {{cookiecutter.north_tool_name}} - NORTH Jupyter Tool

This directory contains the NORTH tool configuration and Docker image for running JupyterLab within the NOMAD NORTH (NOMAD Oasis Remote Tools Hub) environment.

## Overview

The {{cookiecutter.north_tool_name}} NORTH tool provides a containerized JupyterLab environment specifically configured for working with data from the {{cookiecutter.plugin_name}} plugin. It allows users to interactively analyze, visualize, and process
data associated with {{cookiecutter.north_tool_name}}.

## Features

- **Pre-configured JupyterLab**: Based on the Jupyter scipy-notebook image with additional scientific computing libraries
- **Custom Extensions**: Includes specialized tools like jupyterlab-h5web for HDF5 file visualization
- **Isolated Environment**: Each user gets their own containerized workspace with the necessary dependencies

## Docker Image

The Docker image is built from `Dockerfile` and includes:

- **Base Image**: Jupyter scipy-notebook (includes NumPy, SciPy, Pandas, Matplotlib, etc.)
- **Node.js 24**: For JupyterLab extensions
- **uv Package Manager**: Fast Python package installation
- **Custom Dependencies**: Defined in the `north_jupyter` optional dependency group in `pyproject.toml`

### Key Dependencies

- `jupyterlab`: Interactive computing environment
- `ipywidgets`: Interactive widgets for Jupyter notebooks

## Configuration

The NORTH tool is configured in `__init__.py` with the following settings:

```python
tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for {{cookiecutter.plugin_name}}',
    image='ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}:latest',
    description='Jupyter Notebook server in NOMAD NORTH for {{cookiecutter.plugin_name}}',
    file_extensions=['ipynb'],
    display_name='{{cookiecutter.north_tool_name}}',
    default_url='/lab',
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    with_path=True,
)
```

### Configuration Options

- **image**: The Docker image location (automatically published to GitHub Container Registry)
- **file_extensions**: File types that trigger this tool (`.ipynb` notebooks)
- **mount_path**: Where NOMAD data can be mounted in the container
- **default_url**: Opens JupyterLab by default (vs classic Jupyter Notebook)

## Building the Docker Image

The Docker image is automatically built and published via GitHub Actions when you include NORTH tools in your plugin. The workflow is defined in `.github/workflows/publish_north.yml`.

### Manual Build

To build the image manually:

```bash
cd {{cookiecutter.plugin_name}}
docker build -f src/{{cookiecutter.module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile \
    -t ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}:latest .
```

## Usage in NOMAD

Once NOMAD database is mounted, users can:

1. Navigate to their `NOMAD` -> `ANALYSE` (menu) 
2. Click on the `NOMAD Remote Tools Hub` menu
3. Select "{{cookiecutter.north_tool_name}}"
4. The JupyterLab environment will launch with access to their data

## Customization

### Adding Python Packages

Add packages to the `north_jupyter` optional dependency group in `pyproject.toml`:

```toml
[project.optional-dependencies]
north_jupyter = [
    "jupyterlab",
    "your-custom-package>=1.0.0",
    # ... other packages
]
```

### Adding System Dependencies

Edit `Dockerfile` to install system packages:

```dockerfile
RUN apt-get update \
 && apt-get install --yes --quiet --no-install-recommends \
      your-system-package \
      another-package
```

### JupyterLab Extensions

Install JupyterLab extensions in the Dockerfile:

```dockerfile
RUN pip install your-jupyterlab-extension && \
    jupyter lab build
```

## Development

### Testing Locally

To test the Docker image locally:

```bash
# Build the image
docker build -f src/{{cookiecutter.module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile -t test-jupyter .

# Run the container
docker run -p 8888:8888 test-jupyter

# Access JupyterLab at http://localhost:8888
```

### Debugging

To debug issues:

```bash
# Run with shell access
docker run -it test-jupyter /bin/bash

# Check installed packages
uv pip list

# Verify JupyterLab installation
jupyter lab --version
```

## Troubleshooting

### Common Issues

1. **Image fails to build**: Check that all dependencies are compatible with Python 3.10+
2. **JupyterLab won't start**: Verify Node.js version >= 20 for JupyterLab 4.4.10+ and/or verify if libraries in conda environment of base image are overwritten (difference between base image and build image) using `pip list` command. It is expected that libraries from the base image will remain untouched.
3. **Missing packages**: Ensure packages are listed in both `pyproject.toml` and `requirements.txt`. If packages are missing, please regenerate the `requirements.txt` file using the command on top of the `requirements.txt` file.

### Support

For issues specific to this NORTH tool, please contact:
- **Maintainer**: {{cookiecutter.full_name}} ({{cookiecutter.email}})
- **Repository**: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}

For general NOMAD NORTH questions, refer to the [NOMAD documentation](https://nomad-lab.eu/prod/v1/docs/).
