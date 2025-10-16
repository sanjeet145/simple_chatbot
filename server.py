from flask import Flask, request, jsonify
from chat_app import get_response
from logger import logger
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

secret_key = os.getenv("SECRET_KEY")


@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"An error occurred: {e}")
    return jsonify({"error": "An internal error occurred."}), 500

@app.route('/chat', methods=['POST'])
def chat():
    logger.info(request)
    data = request.json
    key = data.get('key', '')
    if key != secret_key:
        return jsonify({'error': 'Unauthorized'}), 401
    question = data.get('question', '')
    answer = get_response(question)
    return jsonify({'answer': answer})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)