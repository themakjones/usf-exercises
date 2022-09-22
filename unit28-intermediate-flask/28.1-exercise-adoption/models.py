from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    db.app = app
    db.init_app(app)

pet_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSigYq1kqyDo4tAfLLwPkE3_px4Pmi4FFAuOw&usqp=CAU'

class Pet(db.Model):
    """Pet class"""

    __tablename__ = 'pets'

    def __repr__(self):
        """Show pet info"""
        
        return f"<Pet {self.id} {self.name} {self.species}>"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(15), nullable=False)
    breed = db.Column(db.String(50), default='Unknown')
    photo_url = db.Column(db.String, default=pet_img)
    age = db.Column(db.String(15))
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)