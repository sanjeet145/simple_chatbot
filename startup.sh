pip install -r requirements.txt
gunicorn server:app --bind 0.0.0.0:8000 --workers 4
# uvicorn server:chatapp --reload --host 0.0.0.0 --port 8000 