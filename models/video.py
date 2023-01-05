from videos import db, ma
from sqlalchemy import Column, Integer, String
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class Video(db.Model):
    __tablename__ = "video"
    id=Column(Integer, primary_key=True)
    name=Column(String(100),nullable=False)
    likes=Column(Integer, nullable=False, default=0)
    views=Column(Integer, nullable=False, default=0)

    def __init__(self, name="", likes=0, views=0):
        self.name=name
        self.likes=likes
        self.views=views

    def __repr__(self):
        return(f"Video(id={self.id}, name={self.name}, views = {self.views}, likes = {self.likes}")

    def save(self):
        db.session.add(self)
        db.session.commit()

class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Video
    id = ma.auto_field()
    name = ma.auto_field()
    likes = ma.auto_field()
    views = ma.auto_field()