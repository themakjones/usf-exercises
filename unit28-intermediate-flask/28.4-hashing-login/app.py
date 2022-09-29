from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtention
from models import User, connect_db, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jY*j9t79Jhf8'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtention(app)

connect_db(app)
db.create_all()