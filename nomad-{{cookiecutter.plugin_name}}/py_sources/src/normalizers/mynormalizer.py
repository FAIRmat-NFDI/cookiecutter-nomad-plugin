from nomad.config import config
from nomad.normalizing import Normalizer

configuration = config.get_plugin_entry_point('nomad_{{cookiecutter.module_name}}.normalizers:mynormalizer')

c class MyNormalizer(Normalizer):

    def normalize(self, archive, logger):
        super().normalize(logger)
        logger.info(f'MyNormalizer.normalize: parameter={configuration.parameter}')
        if archive.results and archive.results.material:
            archive.results.material.elements = ['C', 'O']
