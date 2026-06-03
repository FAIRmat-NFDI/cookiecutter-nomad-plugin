from fastapi import FastAPI
from nomad.config import config

api_entry_point = config.get_plugin_entry_point(
    '{{cookiecutter.module_name}}.apis:api_entry_point'
)

app = FastAPI(root_path=f'{config.services.api_base_path}/{api_entry_point.prefix}')


@app.get('/')
async def root():
    return {'message': 'Hello World'}
