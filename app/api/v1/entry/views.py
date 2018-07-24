import random
import datetime
from flask import Blueprint, request, jsonify
from app.api.v1.entry.models import Entry

mod = Blueprint('entry', __name__)

entryIds = []
entries_list = []


def generate_entryId():
    entryId = random.randint(1,100)
    if entryId in entryIds:
        entryId = random.randint(1,1000)
        entryIds.append(entryId)
    return entryId


def get_entry_by_entryId(entryId):
    for entry in entries_list:

        if entry.entryId == int(entryId):
            return entry
    return None

def convert_entry_to_dict(entry):
    if not entry:
        return {}
    return dict([
            ('entryId', entry.entryId),
            ('date', entry.date),
            ('title', entry.title),
            ('details', entry.details)
        ])


@mod.route('/', methods=['POST', 'GET'])
def entry():

    if request.method == 'POST':

        data = request.get_json(force=True)
        entryId = generate_entryId()
        title = data.get("title", None)
        details = data.get("details", None)
        date = datetime.datetime.now()
        user_entry = Entry(entryId, date, title, details)
        entries_list.append(user_entry)

        return jsonify({
            "message" : "Entry successfully added",
            "data": convert_entry_to_dict(user_entry)
        }), 201

    if request.method == 'GET':

        all_entries = []

        for each_entry in entries_list:
            each_entry = convert_entry_to_dict(each_entry)
            all_entries.append(each_entry)
        
        return jsonify({
            "message" : "All entries successfully retrieved",
            "data" : all_entries
        }), 200
    


@mod.route('/<entryId>', methods=['PUT', 'GET'])       
def indiv_entry(entryId): 
    one_entry = get_entry_by_entryId(entryId) 

    if not one_entry:
        return jsonify({
            "message" : "Entry not found",
            "status": False}), 203

    if request.method == 'GET':  
        return jsonify({
            "message": "Entry successfully retrieved",
            "status": True,
            "data": convert_entry_to_dict(one_entry)
            }), 200

    if request.method == 'PUT':
        data = request.get_json(force = True)

        for key, value in data.items():
            if key == "date":
                one_entry.date = value
            elif key  == "title":
                one_entry.title = value
            elif key  == "details":
                one_entry.details = value
            
        return jsonify({
            "message": "Entry successfully updated",
            "status": True,
            "data": convert_entry_to_dict(one_entry)
            }), 200