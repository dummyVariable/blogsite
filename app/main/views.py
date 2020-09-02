
from flask import render_template, redirect

from app.main import main
from .forms import PostForm
from app.models import Post, User, db

user1 = User(username='dude')
user1.password = 'dude'

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@main.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        post = Post(title=title,body=body, user=user1)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('post.html', form=form)