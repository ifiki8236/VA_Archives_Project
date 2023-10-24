from flask import Flask, jsonify
from pull_images import db_pull
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)

@app.route('/', methods=['GET'])
def hello_world():
    data= db_pull()
    return jsonify(data)