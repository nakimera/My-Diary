from flask import Flask
import os
from app.config import app_config
from app.api.v1.auth.models import db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[str(config_name)])
    db.init_app(app)

    from app.api.v1.entry.views import mod as entry
    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(entry, url_prefix='/api/v1/entries')
    app.register_blueprint(auth, url_prefix='/api/v1/auth')

    return app

app = create_app('development')
