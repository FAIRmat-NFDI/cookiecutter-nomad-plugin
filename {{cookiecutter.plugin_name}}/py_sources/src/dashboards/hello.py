"""Hello-world internal dashboard for the cookiecutter plugin template.

The dashboard is a tiny FastAPI app: NOMAD mounts it under
``{api_base_path}/dashboards/{{cookiecutter.module_name}}-hello/`` at
startup. The page calls the authenticated ``/api/v1/users/me`` endpoint
and greets the logged-in user. Because the dashboard is served
same-origin with NOMAD, the ``Authorization`` cookie set by the NOMAD
GUI is carried along automatically — so protected endpoints work
without any CORS or token handoff plumbing. If no user is logged in,
the dashboard renders a "please log in" prompt.
"""

from nomad.config.models.plugins import DashboardEntryPoint

_PAGE = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{cookiecutter.plugin_name}} — hello</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 2rem; max-width: 720px; }
    h1 { margin-bottom: 0.25rem; }
    code { background: #f2f2f2; padding: 0.1rem 0.4rem; border-radius: 4px; }
    .muted { color: #888; }
    .err { color: #c33; }
    .ok { color: #2a7; font-weight: 600; }
    dl { display: grid; grid-template-columns: max-content 1fr; gap: 0.25rem 1rem; margin-top: 1rem; }
    dt { font-weight: 600; color: #444; }
    dd { margin: 0; font-family: 'SF Mono', Menlo, monospace; font-size: 0.95rem; }
  </style>
</head>
<body>
  <h1 id="greeting">Hello from {{cookiecutter.plugin_name}}!</h1>
  <p class="muted">
    This page is served by a FastAPI instance returned from
    <code>DashboardEntryPoint.load()</code>. It calls the authenticated
    endpoint <code id="endpoint">…</code> in your browser and greets the
    logged-in user. Because the dashboard is same-origin with NOMAD,
    the GUI's <code>Authorization</code> cookie is sent automatically —
    no CORS or token handoff needed.
  </p>
  <p id="status" class="muted">Checking your session…</p>
  <dl id="info" hidden></dl>

  <script>
    (function () {
      var apiBase = window.location.pathname.replace(/\\/dashboards\\/[^/]+\\/?$/, '')
        + '/api/v1';
      var endpoint = apiBase + '/users/me';
      document.getElementById('endpoint').textContent = endpoint;

      var status = document.getElementById('status');
      var info = document.getElementById('info');
      var greeting = document.getElementById('greeting');

      fetch(endpoint, {credentials: 'same-origin'})
        .then(function (r) {
          if (r.status === 401) {
            var e = new Error('Not authenticated');
            e.status = 401;
            throw e;
          }
          if (!r.ok) throw new Error('HTTP ' + r.status);
          return r.json();
        })
        .then(function (user) {
          var name = (user.first_name || user.username || 'there').trim();
          greeting.textContent = 'Hello, ' + name + '!';
          status.textContent = 'You are logged in.';
          status.className = 'ok';
          info.hidden = false;
          var fields = [
            ['Username', user.username || '–'],
            ['Email', user.email || '–'],
            ['User id', user.user_id || '–'],
            ['Affiliation', user.affiliation || '–'],
          ];
          fields.forEach(function (row) {
            var dt = document.createElement('dt');
            dt.textContent = row[0];
            var dd = document.createElement('dd');
            dd.textContent = row[1];
            info.appendChild(dt);
            info.appendChild(dd);
          });
        })
        .catch(function (err) {
          if (err.status === 401) {
            status.innerHTML = 'Not logged in — please '
              + '<a href="javascript:window.top.location.reload()">log in via the NOMAD GUI</a>'
              + ' and reload.';
            status.className = 'err';
          } else {
            status.textContent = 'Failed: ' + err.message;
            status.className = 'err';
          }
        });
    })();
  </script>
</body>
</html>
"""


class HelloDashboardEntryPoint(DashboardEntryPoint):
    def load(self):
        from fastapi import FastAPI
        from fastapi.responses import HTMLResponse

        app = FastAPI()

        @app.get('/', response_class=HTMLResponse)
        async def index():
            return _PAGE

        return app


hello_dashboard_entry_point = HelloDashboardEntryPoint(
    name='Hello, NOMAD',
    id_url_safe='{{cookiecutter.module_name}}-hello',
    description=(
        'A hello-world dashboard that mounts a FastAPI app inside '
        'NOMAD and calls the authenticated /api/v1/users/me endpoint '
        'to greet the logged-in user.'
    ),
    launch_modes=['embedded', 'tab'],
)
