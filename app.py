"""Fire Drill Attendance — Phase 1, served inside Streamlit.

The UI itself is the Phase 1 single-file HTML/JS app
(fire-drill-attendance.html): teacher headcount, student self-report
and coordinator dashboard. Streamlit only wraps it.
Until a Google Apps Script backend URL is set in the app Settings,
it runs in demo mode (local only, not shared). With a URL set, it
reads/writes the shared Google Sheet via that bridge.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Fire Drill Attendance",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the app fills the page like a mobile app.
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "fire-drill-attendance.html"
html = html_path.read_text(encoding="utf-8")

components.html(html, height=900, scrolling=True)
