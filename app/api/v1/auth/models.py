import uuid

class User(object):

    def __init__(self, username, emailAddress, password, admin):
        self.id = int(uuid.uuid1())
        self.username = username
        self.emailAddress= emailAddress
        self.password = password
        self.admin = bool()


    