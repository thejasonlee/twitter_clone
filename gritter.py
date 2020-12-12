from project import app, db
from flask import render_template
from project.models import User, Post, Message
from project.db_queries import *


@app.route('/')
def home():
    posts = Post.query.all()
    like_counts = []
    for post in posts:
        like_counts.append(get_likes_by_post_id(post.id))


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message}


if __name__ == '__main__':
    app.run(debug=True)
