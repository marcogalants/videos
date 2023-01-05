from flask import Blueprint, request, jsonify
from videos import db, printlog, getHumanReadableSize, setMachineReadableSize
import json
from models.video import Video, VideoSchema

video = Blueprint("video", __name__, template_folder="templates", static_folder="static")

@video.route("/",methods=['GET'])
def getAllVideos():
    videos=Video.query.all()
    video_schema = VideoSchema(many=True)
    output = video_schema.dump(videos)
    return jsonify({'video': output}), 200

@video.route("/<int:video_id>",methods=['GET'])
def getVideo(video_id):
    if video_id:
        video = Video.query.filter_by(id=video_id).first()
        if video:
            video_schema = VideoSchema()
            output = video_schema.dump(video)
            return jsonify({'video': output}), 200
        else:
            return jsonify(message="video not found"), 404
    else:
        return jsonify(message="video id not specified"), 404
        
@video.route("/",methods=['POST'])
def createVideo():
    # get input body (data) and create a new video record in the DB returning http status 201 in case of success
    data=json.loads(request.data)
    video=Video(data['name'], data['likes'], data['views'])
    try:
        db.session.add(video)
        db.session.commit()
        return "new video created", 201
    except Exception as e:
        return "could not complete new video creation: " + e, 500

@video.route("/<int:video_id>", methods=['PATCH'])
def modifyVideo(video_id):
    if video_id:
        video = Video.query.filter_by(id=video_id).first()
        data = json.loads(request.data)
        if video:
            try:
                for attr in video.__dict__.keys():
                    if attr in data.keys():
                        setattr(video, attr, data[attr])
                """
                if 'views' in data.keys():
                    video.views = int(data['views'])
                if 'likes' in data.keys():
                    video.likes = int(data['likes']) 
                """
                db.session.add(video)
                db.session.commit()
                return jsonify(message="video modified"), 201
            except Exception as e:
                return jsonify(message="could not modify video: " + e), 500
        else:
            return jsonify(message="video id not specified"), 404

@video.route("/<int:video_id>", methods=['DELETE'])
def deleteVideo(video_id):
    if video_id:
        video = Video.query.filter_by(id=video_id).first()
        if video:
            try:
                db.session.delete(video)
                db.session.commit()
                return jsonify(message=f'Video id {video_id} deleted successfully'), 204
            except Exception as e:
                return jsonify(message="could not modify video: " + e), 404
    return jsonify(message=f'wrong parameter'), 500