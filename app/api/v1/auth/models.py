import uuid
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email_address = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(30))


    def __init__(self, username, email_address, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.email_address= email_address
        self.password =  password


