
from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    chat_id = db.Column(db.JSON, nullable=True, default=list)
    settings = db.Column(db.JSON, nullable=True, default={"cpu": 85, "ram": 10, "disk": 10, "temperature": 45})
    interval = db.Column(db.Integer, nullable=True, default=5)

    def __repr__(self):
        return f"<User with name {self.username} and id {self.id}>"

    def get_id(self):
        return self.id

