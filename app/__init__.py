from flask import Flask
from app.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])
    
    from app.api.v1.entry.views import mod as entry
    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(entry, url_prefix='/api/v1/entries')
    app.register_blueprint(auth, url_prefix='/api/v1/users')

    return app