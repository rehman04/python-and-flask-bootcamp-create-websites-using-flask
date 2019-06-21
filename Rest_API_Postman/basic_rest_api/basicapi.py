import os
from flask import Flask
from flask_restful import Resource,Api#Resource to connect to ,USING rest api
#api is wrapper to entire application that allows Resource to connect
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLAlCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=True
db=SQLAlchemy(app)
Migrate(app,db)

api=Api(app)
jwt=JWT(app,authenticate,identity)

#now creating model instead of list
#kittens=[]
class Kitten(db.Model):
    __tablename__="kits"
    name=db.Column(db.String(80),primary_key=True)
    def __init__(self,name):
        self.name=name
    def json(self):
        return {'name':self.name}


class KittenNames(Resource):
    def get(self,name):
        kit =Kitten.query.filter_by(name=name).first()
        if kit:
            return kit.json()
        else:
            return {'name':None},404

        """for kit in kittens:
            if kit['name'] ==name:
                return kit"""

    def post(self,name):
        kit =Kitten(name=name)
        db.session.add(kit)
        db.session.commit()
        return kit.json()

        '''{'name':name}
        kittens.append(kit)
        return kit'''


    def delete(self,name):
        kit=Kitten.query.filter_by(name=name).first()
        db.session.delete(kit)
        db.session.commit()

        '''for ind,kit in enumerate(kittens):
            if kit['name']==name:
                deleted_kit=kittens.pop(ind)'''
        return {'note':'delete success'}

class ALlNames(Resource):
    # @jwt_required()
    def get(self):
        # return {'kittens':kittens}
        kittens=Kitten.query.all()
        return [kit.json() for kit in kittens]

api.add_resource(KittenNames,'/kitten/<string:name>')#request to home page('/')
api.add_resource(ALlNames,'/kittens')
if __name__=='__main__':
    app.run(debug=True)
