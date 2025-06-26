from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.parsers.parser import NewParser

        return NewParser(**self.model_dump())


class {{cookiecutter.lab_name}}ExperimentParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.parsers.{{cookiecutter.lab_name}}_batch_parser import {{cookiecutter.lab_name}}ExperimentParser

        return {{cookiecutter.lab_name}}ExperimentParser(**self.model_dump())


class {{cookiecutter.lab_name}}ParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.parsers.{{cookiecutter.lab_name}}_measurement_parser import {{cookiecutter.lab_name}}Parser

        return {{cookiecutter.lab_name}}Parser(**self.model_dump())


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


{{cookiecutter.lab_name}}_experiment_parser_entry_point = {{cookiecutter.lab_name}}ExperimentParserEntryPoint(
    name='{{cookiecutter.lab_name}}ExperimentParserEntryPoint',
    description='{{cookiecutter.lab_name}} experiment parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)


{{cookiecutter.lab_name}}_parser_entry_point = {{cookiecutter.lab_name}}ParserEntryPoint(
    name='{{cookiecutter.lab_name}}ParserEntryPoint',
    description='{{cookiecutter.lab_name}} parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)
