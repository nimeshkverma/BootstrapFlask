#!flask/bin/python
from config import configure_and_run_server
from app import app

if __name__ == "__main__":
    configure_and_run_server(app, 'config.DevelopmentConfig')
