from flask import Blueprint, request, jsonify, make_response
from werkzeug.security import generate_password_hash
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)

@mod.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username")
        email_address = data.get("email_address")
        password = generate_password_hash(data.get("password"), method='sha256')

        if username == "" or password == "":
            return make_response('Please fill all fields', 400)
        user = User(username, email_address, password)
        
        return jsonify({"message": "User sucessfully created"}), 201

@mod.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = User.encode_token()
        return make_response('logged in' + token.decode(), 200)

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required'}), 401


@mod.route('/protected')
def protected():
    pass

@mod.route('/unprotected')
def unprotected():
    pass