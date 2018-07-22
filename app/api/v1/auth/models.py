# import app.config
import uuid

class User(object):

    def __init__(self, username, emailAddress, password, admin):
        self.id = int(uuid.uuid1())
        self.username = username
        self.emailAddress= emailAddress
        self.password = password
        self.admin = bool()

    def encode_token(seld, id):
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
        