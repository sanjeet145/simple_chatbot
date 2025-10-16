# pip install -r requirements.txt
# python -m gunicorn server:app --bind 0.0.0.0:8000 --workers 4  # its failling in netlify thats why using added python -m
# uvicorn server:chatapp --reload --host 0.0.0.0 --port 8000 

docker build -t chatbot_image .
docker run -d -p 8000:8000 --name chatbot_container chatbot_image