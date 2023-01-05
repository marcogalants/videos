from flask import request, jsonify
from videos import app

@app.route("/", methods=["GET"])
def root():
    return jsonify({'message': 'please use /videos path to invoke this API'}), 200