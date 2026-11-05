"""Fire Drill Attendance app, served inside Streamlit.

The attendance UI itself is the original single-file HTML/JS app
(fire-drill-attendance.html). Streamlit only wraps it, so the app keeps its
editable class names, add/remove classes, editable student totals per class,
No class toggles, dashboard totals, absent counts and copyable summary
exactly as built.
Counts live in the browser, just like the original app.
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
