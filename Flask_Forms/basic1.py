from flask import Flask,render_template,request,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,TextField,TextAreaField,SubmitField,RadioField,
                      BooleanField,DateTimeField,SelectField)
from wtforms.validators import DataRequired
app=Flask(__name__)

app.config["SECRET_KEY"]='mykey'

class Infoform(FlaskForm):
    breed=StringField("what breed are you", validators=[DataRequired()])
    neutered=BooleanField("have u been neuter?")
    mood=RadioField("please choose ur mood:",
                    choices=[('mood_one','happy'),('mood_two',"unhappy")])
    food=SelectField(u"pick ur favorite food",
                      choices=[('chi','chicken'),('fis','fish'),('bf','beef')])
    feedback=TextAreaField()
    submit=SubmitField('Submit')
@app.route('/',methods=['GET','POST'])
def index():
    form=Infoform()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['food']=form.food.data
        session['feedback']=form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template('index1.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug=True)
