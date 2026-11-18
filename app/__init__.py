from flask import Flask
from app.config import Config
from app.routes.health import health_bp


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Rejestracja blueprintów (warstwa prezentacji)
    app.register_blueprint(health_bp, url_prefix="/api")

    return app