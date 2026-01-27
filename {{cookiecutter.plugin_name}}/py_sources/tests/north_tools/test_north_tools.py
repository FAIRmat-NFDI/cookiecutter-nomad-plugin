def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from {{cookiecutter.module_name}}.north_tools.{{cookiecutter.north_tool_name}} import (
        {{cookiecutter.__north_tool_EP_name}},
    )

    assert (
        {{cookiecutter.__north_tool_EP_name}}.id_url_safe == '{{cookiecutter.module_name}}_{{cookiecutter.north_tool_name}}'
        or {{cookiecutter.__north_tool_EP_name}}.id == 'nomad-north-{{cookiecutter.plugin_name}}'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
