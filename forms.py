"""Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

species_choices = SelectField('Species',
                              choices=[('cat', 'Cat'), ('dog', 'Dog')]
                              )


class PetForm(FlaskForm):
    """Form for adding/editing pet."""

    name = StringField("Name", validators=[InputRequired()])

    species = SelectField('Species',
                          choices=[('cat', 'Cat'), ('dog', 'Dog'), ('chipmunk', 'Chipmunk'), ('porcupine', 'Porcupine')], validators=[InputRequired()])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])

    notes = StringField("Notes", validators=[Optional()])

    available = BooleanField("Available", default=True)
