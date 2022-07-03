# loader/views.py

from flask import render_template, Blueprint, send_from_directory
from utils import create_post

# Добавим настройку директории с шаблонами
loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='templates',
)


@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post_uploaded", methods=["POST"])
def page_post_upload():
    pic, text, cat_name, template = create_post()
    return render_template(template, pic=pic, cat_name=cat_name,
                           text=text)


@loader_blueprint.route("/uploads/<path:path>")
def upload_dir(path):
    return send_from_directory("uploads", path)
