# main/views.py

# Добавим импорт шаблонизатора

from flask import render_template, Blueprint, request
from utils import load_posts, get_posts_by_word

# Добавим настройку папки с шаблонами
main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    # template_folder='templates',
)


# Добавим render_template
@main_blueprint.route('/')
def main_page():
    posts = load_posts()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/search_page')
def search_page():
    return render_template("search.html")


# Добавим render_template
@main_blueprint.route('/search', methods=["GET"])
def search():
    s = request.args['s']
    posts = get_posts_by_word(s)

    return render_template("search.html", posts=posts, search=s)
