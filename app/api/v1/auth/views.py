from flask import Blueprint, request, jsonify, make_response
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.api.v1.auth.models import User
# import app.config

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
                    ('id', user.id),
                    ('username', user.username),
                    ('password', user.password),
                    ('emailAddress', user.emailAddress)
                ])
            all_users.append(user)
        
        return jsonify({
            "message" : "All users successfully retrieved",
            "users" : all_users,
            }), 200

@mod.route('/login', methods=['POST'])
def login_user(): 
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Please fill all fields', 401, {"WWW-Authenticate" : 'Basic realm="Login required!"'})
    
    for user in users_list:
        if not user:
            return make_response('could not verify', 401, {"WWW-Authenticate" : 'Basic realm="Login required!"'})

        if check_password_hash(user.password, auth.password):
        #     token = jwt.encode(
        #         {
        #             'id' : user.id, 
        #             'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        #         }, 
        #         app.config.get('SECRET_KEY')
        #     )
        #     return jsonify({"token" : token})

        # data = request.get_json()
        # if data.get('username') == user.username and data.get('password_hash') == user.password:
        #     return jsonify({
        #         "message": "{} logged in". format(user.username),
        #         "data" : user.id,
        #         "status": False
        #                 }), 200        

            