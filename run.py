import os
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)
port = int(os.environ.get("PORT",5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)