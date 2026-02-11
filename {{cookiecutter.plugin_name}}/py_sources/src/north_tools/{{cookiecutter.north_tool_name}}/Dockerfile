ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-jupyter
ARG PLUGIN_NAME={{cookiecutter.plugin_name}}

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

# This Dockerfile intentionally only selects a NORTH base image.
#
# Its purpose is to provide a minimal and reproducible starting point for
# building a custom NOMAD NORTH tool image. The base image already contains
# the complete NORTH runtime environment (e.g. JupyterLab or desktop setup),
# while this repository defines where tool-specific extensions should be added.
#
# By default, the resulting image is identical to the selected base image.
# Users are expected to extend this Dockerfile to install their plugin and
# add any additional dependencies or configuration required by the tool.
#
# Base image selection:
#   - Jupyter-based tools:
#       BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-jupyter
#   - Tools requiring a graphical user interface:
#       BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base
#
# Extend this Dockerfile to:
#   - install your plugin
#   - add additional system or Python dependencies
#   - add tool-specific configuration
#
# Reference implementations of NORTH base images:
#   nomad-north-jupyter:
#     https://github.com/FAIRmat-NFDI/nomad-north-jupyter/blob/main/src/nomad_north_jupyter/north_tools/my_north_tool/Dockerfile
#   nomad-north-desktop-base:
#     https://github.com/FAIRmat-NFDI/nomad-north-desktop-base/blob/main/Dockerfile