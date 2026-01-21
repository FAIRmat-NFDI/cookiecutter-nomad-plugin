def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for an app
    from {{cookiecutter.module_name}}.north_tools.{{cookiecutter.module_name}}_jupyter import (
        north_tool_jupyter,
    )

    assert (
        north_tool_jupyter.id_url_safe == 'nomad-north-{{cookiecutter.plugin_name}}'
        or north_tool_jupyter.id == 'nomad-north-{{cookiecutter.plugin_name}}'
    ), 'North tool entry point has incorrect id or id_url_safe'
