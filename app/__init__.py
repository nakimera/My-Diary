from flask import Flask
from app.config import configuration

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(configuration[environment])
    
    from app.api.v1.entry.views import mod as entry

    app.register_blueprint(entry, url_prefix='/api/v1/users')

    return app