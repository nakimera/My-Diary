from flask import Flask
from app.config import configuration

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(configuration["development"])
    
    from app.api.v1.entry.views import mod as entry
    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(entry, url_prefix='/api/v1/entries')
    app.register_blueprint(auth, url_prefix='/api/v1/users')

    return app