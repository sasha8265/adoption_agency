from flask_wtf import FlaskForm
from sqlalchemy import Integer
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    name = StringField(
        "Name", 
        validators=[InputRequired()])
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("hedgehog", "Hedgehog"), ("guinea_pig", "Guinea Pig")])
    photo_url = StringField(
        "Photo URL", 
        validators=[
            Optional(), 
            URL('Must be a valid URL format')])
    age = IntegerField(
        "Age in Years", 
        validators=[
            Optional(), 
            NumberRange(min=0, max=30, message="Age must be in whole years between 0 and 30")])
    notes = TextAreaField(
        "Notes", 
        render_kw={"rows": 10, "cols": 5}, 
        validators=[Optional()])



