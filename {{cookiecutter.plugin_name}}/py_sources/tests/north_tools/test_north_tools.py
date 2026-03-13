def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from {{cookiecutter.module_name}}.north_tools import (
        north_tool,
    )

    assert (
        north_tool.id_url_safe == '{{cookiecutter.module_name | replace("_", "-")}}-{{cookiecutter.north_tool_name | replace("_", "-")}}'
        or north_tool.id == 'nomad-north-{{cookiecutter.plugin_name}}'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
