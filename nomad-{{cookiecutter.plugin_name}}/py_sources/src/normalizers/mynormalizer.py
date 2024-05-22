from nomad.config import config
from nomad.datamodel.datamodel import EntryArchive
from nomad.normalizing import Normalizer
from structlog.stdlib import BoundLogger

configuration = config.get_plugin_entry_point(
    'nomad_{{cookiecutter.module_name}}.normalizers:mynormalizer'
)


class MyNormalizer(Normalizer):
    def normalize(self, archive: EntryArchive, logger: BoundLogger) -> None:
        super().normalize(archive, logger)
        logger.info('MyNormalizer.normalize', parameter=configuration.parameter)
        if archive.results and archive.results.material:
            archive.results.material.elements = ['C', 'O']
