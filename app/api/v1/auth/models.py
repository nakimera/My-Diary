import uuid

class User(object):

    def __init__(self, username, emailAddress, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.emailAddress= emailAddress
        self.password = password


    