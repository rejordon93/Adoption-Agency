from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPets, EditPetForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "oceans1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)
app.app_context().push()
db.create_all()


@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template('home_page.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPets()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(pet_name=pet_name, species=species,
                      photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')

    return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet.id}')
    return render_template('pet_details.html', pet=pet, form=form)
