from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v1.auth.models import User

mod = Blueprint('user', __name__)

users_list = []


@mod.route('/users', methods=['POST', 'GET'])
def users():

    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        email_address = data.get("email_address", None)
        password = generate_password_hash(data.get("password", None), method='sha256')
        admin = data.get("admin", False)
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
                "admin": "{}".format(admin)
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


@mod.route('/login', methods=['POST'])
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.check_password_hash:
        return make_response('Please fill all fields', 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})

    for user in users_list:
        if not user:
            return make_response('could not verify', 401, {"WWW-Authenticate": 'Basic realm="Login required!"'})

        # if check_password_hash(user.password, auth.password):
