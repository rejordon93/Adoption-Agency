from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, URL, AnyOf, Optional, NumberRange


class AddPets(FlaskForm):
    """Form for adding Pets."""

    species_choices = ["cat", "dog", "porcupine"]

    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[AnyOf(species_choices)])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = FloatField('Age', validators=[
                     Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    """Form for editing pet details."""

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes')
    available = BooleanField('Available')
