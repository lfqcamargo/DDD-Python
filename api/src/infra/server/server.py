# src/infra/server/server.py
import logging
from flask import Flask
from flask_cors import CORS
from src.infra.database.settings.connection import db_connection_handler
from src.infra.routes.user_routes import users_route_bp
from src.infra.errors.error_handle import handle_errors


def create_app():
    try:
        db_connection_handler.connect_to_db()

        app = Flask(__name__)
        CORS(app)

        logging.basicConfig(level=logging.DEBUG)
        app.logger.setLevel(logging.DEBUG)

        app.register_blueprint(users_route_bp)

        return app
    except Exception as execption:
        handle_errors(execption)
