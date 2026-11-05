# Fire Drill Attendance

Fire Drill Attendance app, with editable class names, add/remove classes,
editable total students per class, No class toggles, dashboard totals and
a copyable summary.

## Deploy to Streamlit Cloud

1. Push this folder to a GitHub repository (see below).
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app** / **New app**.
4. Select the repository, branch `main`, and main file path `app.py`.
5. Click **Deploy**.

Streamlit only wraps the original single-file HTML app
(`fire-drill-attendance.html`); attendance counts live in the browser,
just like the original app, and are not sent to a server.

## Files

- `app.py` — Streamlit wrapper
- `fire-drill-attendance.html` — the attendance app itself
- `requirements.txt` — Streamlit dependency
