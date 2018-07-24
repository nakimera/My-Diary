import uuid

class User(object):

    def __init__(self, username, email_address, password):
        self.id = int(uuid.uuid1())
        self.username = username
        self.email_address= email_address
        self.password =  password


