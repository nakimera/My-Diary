import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    model for the users
    """

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email_address = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, username, email_address, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.email_address = email_address
        self.password = password


    def encode_token(self, id):
        """
        Generate Authentication Token
        return:string
        """

        try:
            payload = {
                'sub' : id,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=2),
                'iat' : datetime.datetime.utcnow()
                }    
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
                )
        except Exception as e:
            return e

    @staticmethod
    def decode_token(token):
        """
        Decodes the authentication token 
        return integer|string
        """
        
        try:
            payload = jwt.decode(token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid Token. Please log in again'





