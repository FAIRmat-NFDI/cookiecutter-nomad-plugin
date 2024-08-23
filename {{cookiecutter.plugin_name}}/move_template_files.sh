#!/bin/sh

rsync -avh {{cookiecutter.plugin_name}}/ .
rm -rfv {{cookiecutter.plugin_name}}
