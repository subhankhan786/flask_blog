from flask import Blueprint, render_template, request, redirect
from models import db, Post

create_post = Blueprint("create_post", __name__, template_folder="templates", static_folder="static")

@create_post.route('/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']
        new_post = Post(title=title, author=author, content=content)
        print(new_post.title, new_post.author, new_post.content)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/blog')
    return render_template("create.html")

@create_post.route("/<slug>")
def slug(slug):
    pass
