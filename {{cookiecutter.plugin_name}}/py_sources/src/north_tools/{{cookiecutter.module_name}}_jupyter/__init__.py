from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description="Jupyter Notebook server in NOMAD NORTH for NOMAD plugin {{ cookiecutter.plugin_name }}.",
    # image='gitlab-registry.mpcdf.mpg.de/nomad-lab/north/xps:master',
    image="ghcr.io/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_name }}/jupyter:latest",
    description="Jupyter Notebook server in NOMAD NORTH for NOMAD plugin {{ cookiecutter.plugin_name }}.",
    external_mounts=[],
    file_extensions=["ipynb"],
    icon="logo/jupyter.svg",
    image_pull_policy="Always",
    default_url="/lab",
    maintainer=[
        {"email": "{{ cookiecutter.email }}", "name": "{{ cookiecutter.full_name }}"}
    ],
    mount_path="/home/jovyan",
    path_prefix="lab/tree",
    privileged=False,
    with_path=True,
    display_name="nomad-north-{{ cookiecutter.north_tool_name }}",
)

north_tool_jupyter = NorthToolEntryPoint(       
    id_url_safe="nomad-north-{{ cookiecutter.plugin_name }}", north_tool=tool
)