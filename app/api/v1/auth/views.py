from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)


@mod.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        email_address = data.get("email_address", None)
        password = generate_password_hash(data.get("password", None), method='sha256')
        user = User(username, email_address, password)
        
        return jsonify({"message": "User sucessfully created"}), 201

@mod.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        return jsonify({'message' : 'logged in'}), 200
