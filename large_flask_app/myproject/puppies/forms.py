from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField

class AddForm(FlaskForm):
    name=StringField('puppy name')
    submit=SubmitField("Add Puppy")

class DelForm(FlaskForm):
    id = IntegerField("please enter id of puppy which means delete")
    submit=SubmitField('Del Puppy')
