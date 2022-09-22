from flask import Flask, redirect, request, render_template, flash
from models import Pet, connect_db, db
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jY*j9t79Jhf8'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mj_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    """Renders custom 404 page when there is a 404 error"""
    
    return render_template('404.html'), 404

@app.route('/')
def home_page():
    """Home page"""
    pets = Pet.query.filter_by(available=True)

    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add pet to adoption list"""

    if form.validate_on_submit():

