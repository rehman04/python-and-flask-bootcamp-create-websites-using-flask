#create entries into the table
from models import db,Puppy,Owner,Toy
#Creating 2 puppies
rufus =Puppy('Rufus')
fido= Puppy('Fido')
#add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

#check
print(Puppy.query.all())

rufus=Puppy.query.filter_by(name="Rufus").first()#all()[0] -->for all and index zero

#create an owner obj
hux=Owner("hux",rufus.id)

#Give Rufus some toys
toy1=Toy('chew toy',rufus.id)
toy2=Toy('ball',rufus.id)

db.session.add_all([hux,toy1,toy2])
db.session.commit()

#Grab rufus after those additions
rufus=Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
