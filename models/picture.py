from sqlalchemy import Column, Integer, String, VARCHAR
from config import db

class Picture(db.Model):
    __tablename__ = 'picture'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    tag = Column(VARCHAR(20))
    likes = Column(Integer)
    path = Column(VARCHAR(255), nullable=False)

    def __init__(self, name: str, tag: str, path: str, likes=None):
        self.name = name
        self.tag = tag
        self.likes = likes
        self.path = path

    def __repr__(self):
        return self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'tag': self.tag,
            'likes': self.likes,
            'path': self.path
        }