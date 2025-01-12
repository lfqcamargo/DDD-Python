import logging
from flask import Flask
from flask_cors import CORS
from src.infra.database.postgre.settings.connection import db_connection_handler
from src.infra.routes.user_routes import users_route_bp


def create_app():
    """
    Init App
    """
    db_connection_handler.connect_to_db()

    app = Flask(__name__)
    CORS(app)

    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(users_route_bp)

    return app
