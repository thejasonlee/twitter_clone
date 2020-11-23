from project import app
from flask import render_template
from project.models import Post
from project.db_queries import *


@app.route('/')
def home():
    posts = Post.query.all()
    like_counts = []
    for post in posts:
        like_counts.append(get_likes_by_post_id(post.id))

if __name__ == '__main__':
    app.run(debug=True)
