def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from {{cookiecutter.module_name}}.apps import new_app

    assert new_app.app.label == 'NewApp'

