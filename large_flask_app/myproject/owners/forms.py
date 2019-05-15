from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField

class AddForm(FlaskForm):
    name = StringField("Name Of owner")
    pup_id=IntegerField("Id Of Puppy")
    submit=SubmitField('Add Owner')
