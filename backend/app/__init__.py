from flask import Flask
from flask_cors import CORS
from .database import mysql
from .routes import api_bp
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    mysql.init_app(app)

    app.register_blueprint(api_bp)

    return app
