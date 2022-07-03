import json
from config import ALLOWED_EXTENSIONS, POST_PATH, COMMENTS_PATH


def load_json(filepath):
    """Выгружаем посты в список из файла"""

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_json = f.read()

    post_list = json.loads(raw_json)

    return post_list


def load_posts() -> list:
    """Выгружаем посты в список из файла"""

    post_list = load_json(POST_PATH)

    return post_list


def load_comments() -> list:
    """Выгружаем посты в список из файла"""

    post_list = load_json(COMMENTS_PATH)

    return post_list


def is_filename_allowed(filename) -> bool:
    """Проверка на расширение"""

    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True


def get_posts_by_word(user_input):
    """"Получаем список постов по слову из формы поиска"""

    dict_list = load_posts()
    user_input_lower = user_input.lower()
    search_list = []

    for dictionary in dict_list:
        post = dictionary['content']    .lower()
        if user_input_lower in post:
            search_list.append(dictionary)
            continue
    return search_list


def get_post_by_uid(uid):
    dict_list = load_posts()

    for d in dict_list:
        if uid == d['pk']:
            return d


def get_comments_by_uid(uid):
    dict_list = load_comments()
    comments = []

    for d in dict_list:
        if d['post_id'] == uid:
            comments.append(d)

    return comments
