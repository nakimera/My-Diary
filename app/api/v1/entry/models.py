from app.api.v1.auth.models import User

class Entry(User):

    def __init__(self, entryId, date, title, details):
        self.entryId = entryId
        self.date = date
        self.title = title
        self.details = details

