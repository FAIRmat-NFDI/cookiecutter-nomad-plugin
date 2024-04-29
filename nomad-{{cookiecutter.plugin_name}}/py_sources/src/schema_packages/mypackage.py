from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage

configuration = config.get_plugin_entry_point('nomad_{{cookiecutter.module_name}}.schema_packages:mypackage')

m_package = SchemaPackage()


class MySchema(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive, logger):
        super().normalize(archive, logger)

        logger.info(f'MySchema.normalize: parameter={configuration.parameter}')
        self.message = f'Hello {self.name}!'

 
m_package.__init_metainfo__()
