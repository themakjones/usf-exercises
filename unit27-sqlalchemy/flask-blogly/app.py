"""Blogly application."""

from flask import Flask, redirect, request, render_template, flash
from models import db, connect_db, User
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
        full_name = new_user.get_full_name()

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
    return render_template('edit_user.html', user=user)


    
