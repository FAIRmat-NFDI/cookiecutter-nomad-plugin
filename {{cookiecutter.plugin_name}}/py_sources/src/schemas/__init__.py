from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.schemas.schema import m_package
 
        return m_package


schema_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchema',
    description='New schema entry point configuration.',
)
