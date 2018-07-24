from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)

users_list = []


@mod.route('/', methods=['POST', 'GET'])
def users():

    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        email_address = data.get("email_address", None)
        password = generate_password_hash(data.get("password", None), method='sha256')
        user = User(username, email_address, password)
        users_list.append(user)
        return jsonify({
            "message": "User sucessfully created",
            "status": True,
            "data": {
                "id": user.id,
                "username": "{}".format(username),
                "password": "{}".format(password),
                "email_address": "{}".format(email_address),
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
            "message": "All users successfully retrieved",
            "users": all_users,
        }), 200

