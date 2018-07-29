from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[str(config_name)])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Annemellisa1@localhost/mydiary'


    from app.api.v1.entry.views import mod as entry
    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(entry, url_prefix='/api/v1/entries')
    app.register_blueprint(auth, url_prefix='/api/v1/auth')

    return app

app = create_app('development')
db = SQLAlchemy(app)