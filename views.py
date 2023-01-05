from flask import request, jsonify
from videos import app, db, printlog, getHumanReadableSize, setMachineReadableSize
from models.video import Video, VideoSchema

@app.route("/", methods=["GET"])
def root():
    return jsonify({'message': 'please go to /videos to consume video API'}), 200