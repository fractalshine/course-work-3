from flask import Flask
from app_config import Config

# Импортируем блюпринты
from blueprints.main.views import main_blueprint
from blueprints.api.api import api_blueprint
from blueprints.errors.view import error_blueprint
from blueprints.posts.posts import posts_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Регистрируем блюпринты
    app.register_blueprint(main_blueprint)
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_blueprint(error_blueprint)

    return app


app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True)
