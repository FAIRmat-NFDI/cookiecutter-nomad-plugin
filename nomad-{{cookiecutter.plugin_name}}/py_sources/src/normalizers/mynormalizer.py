from nomad.datamodel.metainfo.workflow import Workflow
from nomad.normalizing import Normalizer

class MyNormalizer(Normalizer):

    def normalize(self, archive, logger):
        super().normalize(logger)
        logger.info('ExampleNormalizer called')
        archive.workflow2 = Workflow(name='Example workflow')
