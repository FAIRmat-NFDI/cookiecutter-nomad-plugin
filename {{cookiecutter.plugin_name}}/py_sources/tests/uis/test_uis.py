def test_importing_ui():
    # raises if pydantic validation on the UIEntryPoint fails
    from {{cookiecutter.module_name}}.uis import ui_entry_point

    assert ui_entry_point.external_url.startswith('http')
    assert set(ui_entry_point.launch_modes) <= {'embedded', 'external'}
