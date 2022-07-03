from flask import render_template, Blueprint
import json
from config import logger

# Добавим настройку директории с шаблонами
error_blueprint = Blueprint(
    'error_blueprint',
    __name__,
)


@error_blueprint.app_errorhandler(413)
def file_too_big(e):
    return f'File to big: {e}'


@error_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@error_blueprint.app_errorhandler(json.JSONDecodeError)
def database_corrupted(e):
    message = "Бд повреждена"
    logger.error(f"{message} - {e}")
    return render_template("index_errorpage.html", message=message)


@error_blueprint.app_errorhandler(FileNotFoundError)
def database_missed(e):
    message = "Бд отсутствует"
    logger.error(f"{message} - {e}")
    return render_template("index_errorpage.html", message=message)


@error_blueprint.app_errorhandler(500)
def page_error_500(e):
    message = f"На сервере произошла ошибка - {e}"
    logger.error(f"{message} - {e}")
    return render_template("index_errorpage.html", message=message)


@error_blueprint.app_errorhandler(ValueError)
def page_error_value(e):
    return f'{e}', 500
