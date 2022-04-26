from flask import Flask, request, render_template,  redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "somethinginappropriate"


connect_db(app)



@app.route('/')
def home_page():
    """Render home page with all pets"""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)



@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Add a new pet - render form and handle submit """

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data
        )

        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)



@app.route('/pets/<int:pet_id>')
def view_pet(pet_id):
    """View pet details"""

    pet = Pet.query.get(pet_id)
    return render_template('show_pet.html', pet=pet)



@app.route('/pets/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit existing pet details - render form and handle submit """

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
        