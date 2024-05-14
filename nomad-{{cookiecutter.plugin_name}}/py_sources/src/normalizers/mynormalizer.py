from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.normalizing import Normalizer

configuration = config.get_plugin_entry_point(
    'nomad_{{cookiecutter.module_name}}.normalizers:mynormalizer'
)


class MyNormalizer(Normalizer):
    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        logger.info('MyNormalizer.normalize', parameter=configuration.parameter)
        if archive.results and archive.results.material:
            archive.results.material.elements = ['C', 'O']
