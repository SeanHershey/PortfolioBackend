from flask import Flask, jsonify, request
from openai import OpenAI
import os
import dotenv

app = Flask(__name__)

dotenv.load_dotenv()

client = OpenAI(
    base_url="https://api.targon.com/v1", 
    api_key=os.environ.get("TARGON_API_KEY")
)

@app.route("/")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get('prompt')

    response = client.chat.completions.create(
        model="deepseek-ai/deepseek-coder-33b-instruct",
        stream=True,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    text = ""

    for chunk in response:
        text = text + chunk.choices[0].delta.content

    response = jsonify({"response": text})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
