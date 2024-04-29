from pydantic import Field
from nomad.config.models.plugins import NormalizerEntryPoint


class MyNormalizerEntryPoint(NormalizerEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_{{cookiecutter.module_name}}.normalizers.mynormalizer import MyNormalizer

        return MyNormalizer(**self.dict())


mynormalizer = MyNormalizerEntryPoint(
    name='MyNormalizer',
    description='Normalizer defined using the new plugin mechanism.',
)
