#set up the db inside __init__.py under myproject folder
from myproject import db
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship("Owner",backref='Puppy',uselist=False)#one to one realtion, puppy to owner
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        if self.owner:
            return f"puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet"

class Owner(db.Model):
    __tablename__='owners'
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id
    def __repr__(self):
        return f"owner name is : {self.name}"
