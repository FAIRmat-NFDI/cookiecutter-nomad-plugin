"""Minimal Streamlit app launched as a standalone process.

Run as:

    streamlit run -m {{cookiecutter.module_name}}.uis.streamlit_app \\
        --server.port 8501 --server.headless true

The NOMAD GUI issues a short-lived launch token and appends it as a
``token`` query parameter. We read it, stash it in session state, and
strip it from the visible URL so it does not leak via browser history,
copy-paste, or the Referer header on outbound links.
"""

import os

import streamlit as st

st.set_page_config(page_title='NOMAD UI Plugin Example', layout='wide')

st.title('NOMAD UI Plugin — Streamlit example')
st.write(
    'This page is served by a standalone Streamlit process and rendered '
    'inside the NOMAD GUI either as an embedded iframe or in a separate tab.'
)

if 'launch_token' not in st.session_state:
    token = st.query_params.get('token')
    if token:
        st.session_state['launch_token'] = token
        del st.query_params['token']

token = st.session_state.get('launch_token')
if token:
    st.success(
        'Received launch token from NOMAD (first 12 chars): '
        f'`{token[:12]}...`'
    )
else:
    st.info('No launch token present — open via the NOMAD GUI to receive one.')

st.subheader('Environment')
st.code(
    '\n'.join(
        f'{k}={v}'
        for k, v in sorted(os.environ.items())
        if k.startswith('NOMAD_')
    )
    or '(no NOMAD_* env vars set)'
)
