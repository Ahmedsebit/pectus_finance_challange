import os
from app.app import create_app

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)

def littlepay():
    return create_app(config_name)

if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.run()