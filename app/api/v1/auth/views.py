from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)

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


@mod.route('/users', methods=['POST', 'GET'])
def users():
    
    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        emailAddress = data.get("emailAddress", None)
        password = generate_password_hash(data.get("password", None), method='sha256')
        admin = data.get("admin", False)
        user = User(username, emailAddress, password, admin)
        users_list.append(user)
        return jsonify({
                "message": "User sucessfully created",
                "status": True,
                "data": {
                    "id" : user.id,
                    "username" : "{}".format(username),
                    "password" : "{}".format(password),
                    "emailAddress" : "{}".format(emailAddress),
                    "admin" : "{}".format(admin)
                    }
                }), 201

    if request.method == 'GET':
        all_users = []

        for user in users_list:
            user = dict([
                    ('username', user.username),
                    ('password', user.password),
                    ('emailAddress', user.emailAddress)
                ])
            all_users.append(user)
        
        return jsonify({
            "message" : "All users successfully retrieved",
            "users" : all_users,
            }), 200