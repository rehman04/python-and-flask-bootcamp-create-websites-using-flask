from basic import db,Puppy

#creates
my_obj=Puppy('rufus',5)
db.session.add(my_obj)
db.session.commit()

#Read
All_puppies=Puppy.query.all()
print(All_puppies)

#Select by id
pup_1=Puppy.query.get(1)
print(pup_1)

#filters
pup_frank = Puppy.query.filter_by(name='frankk')
print(pup_frank.all())

#update
first_puppy=Puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()

#Delete
second_pup=Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

All_puppies=Puppy.query.all()
print(All_puppies)
