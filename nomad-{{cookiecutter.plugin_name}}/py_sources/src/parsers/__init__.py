from pydantic import Field
from nomad.config.models.plugins import ParserEntryPoint


class MyParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Config parameter for this plugin.')

    def load(self):
        from nomad_{{cookiecutter.module_name}}.parsers.myparser import MyParser

        return MyParser(**self.dict())


myparser = MyParserEntryPoint(
    name = 'MyParser',
    description = 'Parser defined using the new plugin mechanism.',
    mainfile_name_re = '.*\.myparser',
)
