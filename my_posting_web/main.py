from app import app, db
from post.blueprint import posts
from home.blueprint import home
from create_post.blueprint import create_post

app.register_blueprint(posts, url_prefix="/blog")
app.register_blueprint(home)
app.register_blueprint(create_post, url_prefix="/create")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)