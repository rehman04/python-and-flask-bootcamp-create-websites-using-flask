from flask import Flask,render_template,session,redirect,url_for,flash,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']='mykey'

class simpleform(FlaskForm):
    submit =SubmitField("Click Me.")
    breed=StringField("What breed are you?",validators=[DataRequired()])

@app.route('/',methods=['GET','POST'])
def index2():
    form=simpleform()
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash('you just changed your breed to : ')
        # flash(f'you just changed your breed to : {session['breed']}') f string interpolation
        return redirect(url_for('index2'))
    return render_template('index2.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
