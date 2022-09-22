from flask_wtf import FlaskForm
from wtforms import StringField

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField('Name')
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('dragon', 'Bearded Dragon')])