from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

# TODO: from forms import Pet form we'll need later

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_homepage():
    """Route for showing our home page"""
    pets = Pet.query.all()

    return render_template('index.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def handle_form_showing_submission():
    """
    Check for form validation. If not a valid post request, then display form again with errors(if any).
    If valid, create the pet and add to database and return to homepage.
    """
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("pet_add.html", form=form)


@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """Show details page for pet with id of pet_id"""
    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet_info.html', pet=pet)


@app.route('/edit/<int:pet_id>', methods=["GET", "POST"])
def handle_pet_edit_form_processing(pet_id):
    """
    Check for form validation. If not a valid post request, then display form again with errors(if any).
    If valid, edit the pet with id of pet_id and send update to database -> Then redirect to pet info page
    """
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect(f"/{pet_id}")
    else:
        return render_template('pet_info_edit.html', pet=pet, form=form)
