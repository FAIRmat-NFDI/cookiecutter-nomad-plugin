#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh {{cookiecutter.plugin_name}}/ .
  rm -rfv {{cookiecutter.plugin_name}}
fi
