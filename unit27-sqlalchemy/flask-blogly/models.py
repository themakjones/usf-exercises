"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model"""
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image_url = db.Column(db.String, default='/static/default_img.jpg')

    @property
    def full_name(self):
        """Gets user's full name """

        full_name = ' '.join([self.first_name, self.last_name])
        return full_name

    posts = db.relationship('Post', back_populates='user', cascade='all, delete')


class Post(db.Model):
    """Post model"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='posts')

    @property
    def friendly_date(self):
        """Display created at in a readable format"""

        return self.created_at.strftime('%A, %b %m, %Y, %I:%M %p')


def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)