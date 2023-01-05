from flask import request, jsonify
from videos import app

@app.route("/", methods=["GET"])
def root():
<<<<<<< HEAD
    return jsonify({'message': 'please use /videos path to invoke this API'}), 200
=======
    return jsonify({'message': 'please go to /video to consume video API'}), 200
>>>>>>> parent of 9aa2c0d (updated endpoint from video to videos)
