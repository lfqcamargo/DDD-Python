# run.py
from src.infra.server.server import create_app

if __name__ == "__main__":
    # Cria a aplicação e sobe o servidor com debug
    app = create_app()
    app.run(host="0.0.0.0", port=3000, debug=True)
