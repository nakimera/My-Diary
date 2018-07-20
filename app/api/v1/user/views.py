from flask import Blueprint, request, jsonify
import jwt
from app.api.v1.user.models import User

mod = Blueprint('user', __name__)

users_list = []    

@mod.route('/unprotected')
def unprotected():
    return 

@mod.route('/protected')
def protected():
    return 

@mod.route('/login')
def login():
    return 


@mod.route('/', methods=['POST', 'GET'])
def users():

    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        emailAddress = data.get("emailAddress", None)
        password = data.get("password", None)
        user = User(username, emailAddress, password)
        users_list.append(user)
        return jsonify({
                "message": "User sucessfully created",
                "status": True,
                "data": {
                    "id" : user.id,
                    "username" : "{}".format(username),
                    "emailAddress" : "{}".format(emailAddress)
                    }
                }), 201

    if request.method == 'GET':
        all_users = []

        for user in users_list:
            user = dict([
                    ('username', user.username),
                    ('emailAddress', user.emailAddress)
                ])
            all_users.append(user)
        
        return jsonify({
            "message" : "All users successfully retrieved",
            "users" : all_users,
            }), 200