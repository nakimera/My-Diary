from flask import Blueprint, request, jsonify
from app.api.v1.user.models import User

mod = Blueprint('user', __name__)


@mod.route('/', methods=['POST', 'GET'])
def users():

    if request.method == 'POST':
        data = request.get_json()
        username = data.get("username", None)
        emailAddress = data.get("emailAddress", None)
        password = data.get("password", None)
        user = User(username, emailAddress, password)
        user.add_user()
        return jsonify({
                "message": "User sucessfully created",
                "status": True,
                "data": {
                    "id" : user.id,
                    "username" : "{}".format(username),
                    "emailAddress" : "{}".format(emailAddress)
                    }
                }), 201

