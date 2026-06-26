def test_importing_hello_dashboard():
    from fastapi import FastAPI

    from {{cookiecutter.module_name}}.dashboards import hello_dashboard_entry_point

    # raises if pydantic validation on the DashboardEntryPoint fails
    assert hello_dashboard_entry_point.external_url is None
    assert set(hello_dashboard_entry_point.launch_modes) <= {'embedded', 'tab'}
    assert isinstance(hello_dashboard_entry_point.load(), FastAPI)
