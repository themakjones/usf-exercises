from flask import Flask, redirect, request, render_template, flash
from models import Pet, connect_db, db
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jY*j9t79Jhf8'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mj_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# @app.errorhandler(404)
# def page_not_found(e):
#     """Renders custom 404 page when there is a 404 error"""
    
#     return render_template('404.html'), 404

@app.route('/')
def home_page():
    """Home page"""
    pets = Pet.query.filter_by(available=True)

    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add pet to adoption list form, handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        breed = form.breed.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, breed=breed, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to adoption list!")
        return redirect('/')


    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_page(pet_id):
    """Pet detail page"""

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data

        db.session.commit()
        flash(f"{pet.name}'s information has been updated!")
        return redirect('/')
    
    return render_template('pet_page.html', pet=pet, form=form)


