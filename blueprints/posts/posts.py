from flask import render_template, Blueprint, request
from utils import get_post_by_uid, get_comments_by_uid
posts_blueprint = Blueprint(
    'posts_blueprint',
    __name__,
    # template_folder='templates',
)


@posts_blueprint.route('/post/<int:pk>')
def post_page(pk):
    post = get_post_by_uid(pk)
    comments = get_comments_by_uid(pk)
    return render_template("post.html", post=post, comments=comments)

