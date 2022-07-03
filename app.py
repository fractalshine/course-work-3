from flask import Flask
from app_config import Config

# from blueprints.loader.views import loader_blueprint
from blueprints.main.views import main_blueprint
from blueprints.api.api import api_blueprint
from blueprints.errors.view import error_blueprint
from blueprints.posts.posts import posts_blueprint


app = Flask(__name__)
app.config.from_object(Config)
# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
# app.register_blueprint(loader_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(error_blueprint)

if __name__ == "__main__":
    app.run()
