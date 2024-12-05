from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get('prompt')
    
    response = jsonify({"response": "Hello World! I am a parrot, " + prompt})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
