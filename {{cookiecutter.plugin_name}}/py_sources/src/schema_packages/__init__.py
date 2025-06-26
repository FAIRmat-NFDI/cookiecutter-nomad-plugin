from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.schema_packages.schema_package import m_package

        return m_package


class {{cookiecutter.lab_name}}PackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from {{cookiecutter.module_name}}.schema_packages.{{cookiecutter.lab_name}}_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)


{{cookiecutter.lab_name}}_schema_package_entry_point = {{cookiecutter.lab_name}}PackageEntryPoint(
    name='{{cookiecutter.lab_name}}Package',
    description='{{cookiecutter.lab_name}} package entry point configuration.',
)
