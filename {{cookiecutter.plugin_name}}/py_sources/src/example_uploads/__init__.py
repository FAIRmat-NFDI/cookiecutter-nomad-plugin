from nomad.config.models.plugins import ExampleUploadEntryPoint

myexampleupload = ExampleUploadEntryPoint(
    title='My Example Upload',
    category='Examples',
    description='Description of this example upload.',
    path='example_uploads/getting_started',
)
