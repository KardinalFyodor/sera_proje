from flask import Flask, request, jsonify

app = Flask(**name**)

@app.route("/")
def home():
return "API calisiyor"

@app.route("/predict", methods=["POST"])
def predict():
return jsonify({"result": "ok"})
