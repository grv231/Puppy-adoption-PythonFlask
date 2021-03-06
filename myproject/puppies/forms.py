from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of the Puppy:')
    submit = SubmitField('Add puppy')

class DelForm(FlaskForm):

    id = IntegerField("Id number of Puppy to remove: ")
    submit = SubmitField("Remove Puppy")
