import os
from forms import AddForm,DelForm
from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"puppy name is: {self.name}"

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/add',methods=['GET','POST'])
def addd():
    form=AddForm()
    if form.validate_on_submit():
        name=form.name.data
        new_pup=Puppy(name)

        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template("add.html",form=form)

@app.route('/list')
def list_pup():
    puppies=Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/delete',methods=['GET','POST'])
def del_pupp():
    del_form=DelForm()
    if del_form.validate_on_submit():
        id=del_form.id.data
        pup=Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template("delete.html",del_form=del_form)

if __name__=='__main__':
    app.run(debug=True)
