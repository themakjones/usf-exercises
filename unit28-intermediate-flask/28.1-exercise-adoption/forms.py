from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField
from wtforms.validators import InputRequired, URL, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Form for adding pet"""

    name = StringField('Name', validators=[InputRequired(message=['Name is required'])])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('dragon', 'Bearded Dragon')], validators=[InputRequired(message=['Please select the species'])])
    breed = StringField('Breed')
    photo_url = StringField('Image Link', validators=[URL(message=['Link must in the the form of a URL'])])
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30, message=['Please enter an age between 0 and 30'])])
    notes = StringField('Notes')