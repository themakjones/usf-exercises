"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)

Default_Img = 'https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
    """Cupcake model"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(25), nullable=False)
    size = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False, default=Default_Img)

    def __repr__(self):
        """Show cupcake info"""

        return f"<Cupcake {self.id} {self.flavor} {self.size}>"

    def serialize(self):
        """Serialize cupcake object to dictionary"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

