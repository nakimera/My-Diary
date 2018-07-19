import uuid

class User(object):

    def __init__(self, id, username, emailAddress, password):
        self.id = int(uuid.uuid3)
        self.username = username
        self.emailAddress= emailAddress
        self.password = password
