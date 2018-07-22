from flask import Blueprint, request, jsonify
import jwt
import datetime
from app.api.v1.user.models import User

mod = Blueprint('user', __name__)

users_list = []    

def generate_token():
    

@mod.route('/unprotected')
def unprotected():
    return 

@mod.route('/protected')
def protected():
    return 

@mod.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password


@mod.route('/', methods=['POST', 'GET'])
def users():
    
    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        email_address = data.get("email_address", None)
        password = data.get("password", None)
        user = User(username, email_address, password)
        users_list.append(user)
        return jsonify({
                "message": "User sucessfully created",
                "status": True,
                "data": {
                    "id" : user.id,
                    "username" : "{}".format(username),
                    "email_address" : "{}".format(email_address)
                    }
                }), 201

    if request.method == 'GET':
        all_users = []

        for user in users_list:
            user = dict([
                    ('username', user.username),
                    ('email_address', user.email_address)
                ])
            all_users.append(user)
        
        return jsonify({
            "message" : "All users successfully retrieved",
            "users" : all_users,
            }), 200