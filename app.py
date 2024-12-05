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

    response = client.completions.create(
        model="deepseek-ai/deepseek-coder-33b-instruct",
        stream=True,
        prompt=prompt,
    )

    for chunk in response:
        if chunk.choices[0].text is not None:
            print(chunk.choices[0].text, end="")

    response = jsonify({"response": "test complete!"})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
