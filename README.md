# Fire Drill Attendance — Phase 1 (shared)

Phase 1 of the comprehensive school fire drill app: shared teacher
headcount, a student self-report view (Safe at assembly point / Still
inside with building, floor, room / Need help, optional note and
optional one-time location), and a live coordinator dashboard
(expected / accounted / missing, classes not yet submitted, missing
list by class, Need help highlighted).

The old, teacher-only version stays live on the Muse public link.
This Phase 1 version is the one deployed to Streamlit.

## Shared store

Google Sheet "Fire Drill Attendance", via a Google Apps Script web
app. Paste the deployed web app URL into the app's Settings >
Shared backend URL field. Until a URL is set, the app runs in a
clearly labelled demo mode (local only, not shared).

Sheet tabs: Classes, TeacherSubmissions, StudentReports, DrillStatus.
Bridge code: workspace/fire-drill-shared/Code.gs, setup in
workspace/fire-drill-shared/SETUP.md.

## Deploy to Streamlit Cloud

1. Push this folder to the GitHub repository.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app** / **New app**.
4. Select the repository, branch `main`, and main file path `app.py`.
5. Click **Deploy**.

## Files

- `app.py` — Streamlit wrapper
- `fire-drill-attendance.html` — the Phase 1 app itself
- `requirements.txt` — Streamlit dependency
