def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from nomad_{{cookiecutter.module_name}}.apps import myapp

    assert myapp.app.label == 'MyApp'

