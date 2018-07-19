import random
from flask import Blueprint, request, jsonify
from app.api.v1.entry.models import Entry

mod = Blueprint('entry', __name__)

entryIds = []
entries_list = []

#generate entryId function
def generate_entryId():
    entryId = random.randint(1,1000)
    if entryId in entryIds:
        entryId = random.randint(1,1000)
        entryIds.append(entryId)
    return entryId

@mod.route('/', methods=['POST', 'GET'])
def entry():
    if request.method == 'POST':

        data = request.get_json(force=True)
        entryId = generate_entryId()
        date = data.get("date", None)
        title = data.get("title", None)
        details = data.get("details", None)
        user_entry = Entry(entry, date, title, details)
        entries_list.append(user_entry)

        return jsonify({
            "message" : "Entry successfully added",
            "data": {
                    "entryId" :"{}".format(entryId) ,
                    "date" : "{}".format(date),
                    "title" : "{}".format(title),
                    "details" : "{}".format(details)
                    }
        }), 201