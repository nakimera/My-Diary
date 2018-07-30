import uuid
import jwt
import datetime
from werkzeug.security import generate_password_hash


class User(object):
    """
    model for the users
    """

    def __init__(self, username, email_address, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.email_address = email_address
        self.password = password


    @staticmethod
    def encode_token(id):
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
                "(SECRET)",
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


    # def hash_password(self, password):
    #     hash_password = generate_password_hash(data.get("password"), method='sha256')

    def verify_password(self, password):
        pass
