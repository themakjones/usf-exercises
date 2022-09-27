"""Flask app for Cupcakes"""

from flask import Flask, redirect, request, render_template, flash
from models import Cupcake, connect_db, db
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