"""Example NOMAD UI plugin backed by a standalone Streamlit process.

The ``UIEntryPoint`` below declares ``external_url``, so NOMAD itself does
not mount the UI — the browser talks directly to the Streamlit process.
Run the Streamlit app separately (see ``streamlit_app.py``) and point
``external_url`` at wherever it is reachable from the user's browser.
"""

from nomad.config.models.plugins import UIEntryPoint

ui_entry_point = UIEntryPoint(
    name='Streamlit example',
    description=(
        'Example user-defined UI served by a standalone Streamlit process. '
        'Demonstrates the UIEntryPoint external_url path and the '
        'launch-token handshake.'
    ),
    external_url='http://localhost:8501',
    launch_modes=['embedded', 'external'],
)
