#!/bin/sh

rsync -avh nomad-{{cookiecutter.plugin_name}}/ .
rm -rfv nomad-{{cookiecutter.plugin_name}}
