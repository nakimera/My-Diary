from flask import Blueprint

mod = Blueprint('entry', __name__)

@mod.route('/')