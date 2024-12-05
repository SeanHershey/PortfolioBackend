from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get('prompt')

    return jsonify({"response": "Hello World! I am a parrot, " + prompt})
