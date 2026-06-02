from nomad.config.models.plugins import APIEntryPoint


class NewAPIEntryPoint(APIEntryPoint):
    def load(self):
        from {{cookiecutter.module_name}}.apis.api import app

        return app


api_entry_point = NewAPIEntryPoint(
    prefix='newapi',
    name='NewAPI',
    description='New API entry point configuration.',
)
