"""Example NOMAD dashboard plugin served as a FastAPI mount inside NOMAD.

NOMAD mounts the FastAPI app returned by ``load()`` under
``{api_base_path}/dashboards/{id_url_safe}/``, so the dashboard is
served same-origin with the rest of NOMAD. That means ``fetch`` calls
to ``{api_base_path}/api/v1/...`` from the dashboard work without any
CORS plumbing, and (when the user is logged in via the NOMAD GUI) the
``Authorization`` cookie is carried along automatically — so protected
endpoints just work too.

This minimal example calls the authenticated ``/api/v1/users/me``
endpoint and greets the logged-in user (or shows a "please log in"
prompt if the visitor has no NOMAD session).
"""

from .hello import hello_dashboard_entry_point

__all__ = ['hello_dashboard_entry_point']
