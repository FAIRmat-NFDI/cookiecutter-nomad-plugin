ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-jupyter
ARG PLUGIN_NAME={{cookiecutter.plugin_name}}

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# Base image may also come from nomad-north-jupyter at https://github.com/FAIRmat-NFDI/nomad-north-jupyter
# e.g., ghcr.io/fairmat-nfdi/nomad-north-jupyter:main
# Please check for details of the base image and Dockerfile at https://github.com/FAIRmat-NFDI/nomad-north-jupyter

# Or base image may also come from nomad-north-destop-base at https://github.com/FAIRmat-NFDI/nomad-north-desktop-base
# e.g., ghcr.io/fairmat-nfdi/nomad-north-desktop-base:main
# Please check for details of the base image and Dockerfile at https://github.com/FAIRmat-NFDI/nomad-north-desktop-base


ARG PLUGIN_NAME
# Copy the plugin source code to the image 
COPY --chown=${NB_USER}:${NB_GID} . ${HOME}/${PLUGIN_NAME}

WORKDIR ${HOME}/${PLUGIN_NAME}

# https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install . --group north


WORKDIR ${HOME}
RUN rm -rf ${HOME}/${PLUGIN_NAME}

RUN jupyter lab build --dev-build=False --minimize=False && \
    fix-permissions "/home/${NB_USER}" \
    && fix-permissions "${CONDA_DIR}"

WORKDIR ${HOME}

EXPOSE 8888

RUN touch ${HOME}/.hushlogin