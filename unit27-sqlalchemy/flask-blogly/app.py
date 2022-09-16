"""Blogly application."""

from flask import Flask, redirect, request, render_template, flash
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dillondainssucks'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    """Renders custom 404 page wher there is a 404 error"""
    
    return render_template('404.html'), 404

@app.route('/')
def home_page():
    """Home page"""

    return redirect('/users')

@app.route('/users')
def users_page():
    """Lists all users"""

    users = User.query.all()

    return render_template('users.html', users=users)

@app.route('/users/new', methods=['POST', 'GET'])
def add_user():
    """Add user page and process add user form"""

    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        img_url = request.form['img-url']
        img_url = img_url if img_url else None

        new_user = User(first_name=first_name, last_name=last_name, image_url=img_url)
        db.session.add(new_user)
        db.session.commit()
        full_name = new_user.full_name

        flash(f"New user: {full_name} added!")
        return redirect('/users')

    return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def user_profile_page(user_id):
    """User profile page"""

    user = User.query.get_or_404(user_id)
    return render_template('user_profile.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST', 'GET'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.first_name = request.form['first-name']
        user.last_name = request.form['last-name']
        img_url = request.form['img-url']
        user.img_url = img_url if img_url else None

        db.session.add(user)
        db.session.commit()

        flash(f"{user.full_name}'s profile has been changed")
        return redirect('/users')

    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):

    
    user = User.query.filter_by(id=user_id)
    user.delete()
    db.session.commit()

    flash('Profile has been deleted')
    return redirect('/users')
    
@app.route('/users/<int:user_id>/posts/new', methods=['POST', 'GET'])
def new_post(user_id):
    """Renders and handles form for submitting new post"""

    user = User.query.get_or_404(user_id)
        
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_post = Post(title=title, content=content, user_id=user.id)
        db.session.add(new_post)
        db.session.commit()
        flash(f"Post: '{new_post.title}' was created!")
        
        return redirect(f'/users/{user.id}')
    return render_template('new_post.html', user=user)

@app.route('/posts/<int:post_id>')
def post_detail_page(post_id):
    """Shows details of a post"""

    post = Post.query.get_or_404(post_id)
    return render_template('post_details.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST', 'GET'])
def edit_post(post_id):
    """Renders edit post form and handles submission of form"""

    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']

        db.session.add(post)
        db.session.commit()

        return redirect('/users')
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):

    
    post = Post.query.filter_by(id=post_id)
    post.delete()
    db.session.commit()

    flash('Post has been deleted')
    return redirect('/users')