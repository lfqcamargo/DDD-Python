# src/infra/server/server.py
import logging
from flask import Flask
from flask_cors import CORS
from src.infra.database.settings.connection import db_connection_handler
from src.infra.routes.user_routes import users_route_bp

def create_app():
    # Conectar ao banco
    db_connection_handler.connect_to_db()

    # Cria a aplicação Flask
    app = Flask(__name__)
    CORS(app)

    # Configuração de logs
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    # Registra o blueprint
    app.register_blueprint(users_route_bp)

    return app
