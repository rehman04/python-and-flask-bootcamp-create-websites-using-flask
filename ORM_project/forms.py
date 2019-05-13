from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField

class AddForm(FlaskForm):
    name=StringField('puppy name')
    add=SubmitField("Add Puppy")

class DelForm(FlaskForm):
    id = IntegerField("please enter id of puppy which means delete")
    Del=SubmitField('Del Puppy')

class OwnerAdd(FlaskForm):
    name_O = StringField("Name Of owner")
    id1=IntegerField("Id Of Puppy")
    Add_O=SubmitField('Add Owner')
