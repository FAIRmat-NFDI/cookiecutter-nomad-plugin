from nomad.config.models.plugins import ExampleUploadEntryPoint

example_upload_entry_point = ExampleUploadEntryPoint(
    title='New Example Upload',
    category='Examples',
    description='Contains the contents of the getting_started folder.',
    resources=['example_uploads/getting_started/*']
)
