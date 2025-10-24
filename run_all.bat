@echo off
echo =========================================================
echo Starting FastAPI backend and Streamlit UI...
echo =========================================================

REM Activate the virtual environment
call .venv\Scripts\activate

REM Start FastAPI (port 8000 by default)
start cmd /k "uvicorn api.main:app --reload --port 8000"

REM Wait a few seconds before launching Streamlit
timeout /t 5 /nobreak >nul

REM Start Streamlit (port 8501 by default)
start cmd /k "streamlit run ui/app.py --server.port 8501"

echo =========================================================
echo Both servers are now running.
echo FastAPI → http://127.0.0.1:8000/docs
echo Streamlit → http://127.0.0.1:8501
echo =========================================================
pause
