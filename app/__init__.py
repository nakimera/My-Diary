from flask import Flask
from app.config import configuration

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(configuration[environment])
    
    from app.api.v1.entry.views import mod as entry
    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(entry, url_prefix='/api/v1/users/entries')
    app.register_blueprint(user, url_prefix='/api/v1/')

    return app