from flask import Flask, jsonify
from .config import Config
from .extensions import db, migrate
from .module_loader import load_modules

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)
    migrate.init_app(app, db)

    @app.get("/api/health")
    def health():
        return jsonify({"ok": True, "data": {"service": "clickdialog-backend"}})

    # Cargar módulos habilitados
    load_modules(app)

    return app
