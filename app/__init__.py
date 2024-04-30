from flask import Flask
from app.routes.views import main

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('app.config.config.Config')
    with app.app_context():
        app.register_blueprint(main)
        return app