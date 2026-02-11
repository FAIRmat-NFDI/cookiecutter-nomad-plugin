def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from {{cookiecutter.module_name}}.north_tools.{{cookiecutter.north_tool_name}} import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == '{{cookiecutter.module_name}}_{{cookiecutter.north_tool_name}}'
        or north_tool_entry_point.id == 'nomad-north-{{cookiecutter.plugin_name}}'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
