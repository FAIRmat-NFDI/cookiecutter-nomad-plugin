import shutil
import os
import pytest
import subprocess


def run_tox(plugin):
    """Run the tox suite of the newly created plugin."""
    tox_plugin_path = os.path.join(plugin, "tox.ini")
    shutil.copy("tox.ini", tox_plugin_path)
    command = [
        "tox",
        "-v",
        "--workdir",
        plugin,
        "-c",
        tox_plugin_path,
        "-e",
        "py",
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("Command Output:")
    print(stdout.decode())
    print(stderr.decode())


@pytest.mark.parametrize("plugin_name", ["foo-bar"])
@pytest.mark.parametrize(
    "include_normalizer",
    [True, False],
)
@pytest.mark.parametrize(
    "include_app",
    [True, False],
)
@pytest.mark.parametrize(
    "include_parser",
    [True, False],
)
@pytest.mark.parametrize(
    "include_schema_package",
    [True, False],
)
def test_run_cookiecutter_and_plugin_tests(
    cookies,
    plugin_name,
    include_normalizer,
    include_app,
    include_parser,
    include_schema_package,
):
    """Create a new plugin via cookiecutter and run its tests."""
    result = cookies.bake(
        extra_context={
            "plugin_name": plugin_name,
            "include_app": str(include_app),
            "include_parser": str(include_parser),
            "include_normalizer": str(include_normalizer),
            "include_schema_package": str(include_schema_package),
        }
    )
    module_name = plugin_name.replace("-", "_")

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == f"nomad-{plugin_name}"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath(
        "src", f"nomad_{module_name}", "__init__.py"
    ).is_file()

    if include_normalizer:
        assert result.project_path.joinpath(
            "src", f"nomad_{module_name}", "normalizers", "mynormalizer.py"
        ).is_file()
    else:
        assert not result.project_path.joinpath(
            "src",
            f"nomad_{module_name}",
            "normalizers",
        ).is_dir()
    if include_app:
        assert result.project_path.joinpath(
            "src", f"nomad_{module_name}", "apps", "__init__.py"
        ).is_file()
    else:
        assert not result.project_path.joinpath(
            "src",
            f"nomad_{module_name}",
            "apps",
        ).is_dir()
    if include_schema_package:
        assert result.project_path.joinpath(
            "src", f"nomad_{module_name}", "schema_packages", "mypackage.py"
        ).is_file()
    else:
        assert not result.project_path.joinpath(
            "src",
            f"nomad_{module_name}",
            "schema_packages",
        ).is_dir()
    if include_parser:
        assert result.project_path.joinpath(
            "src", f"nomad_{module_name}", "parsers", "myparser.py"
        ).is_file()
    else:
        assert not result.project_path.joinpath(
            "src",
            f"nomad_{module_name}",
            "parsers",
        ).is_dir()

    run_tox(str(result.project_path))
