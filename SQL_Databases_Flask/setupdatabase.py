from basic import db,Puppy

#creates all the tables model --> db table
db.create_all()
sam=Puppy('samm',3)
frank=Puppy('frankk',4)
db.session.add_all([sam,frank])
db.session.commit()
print(sam.id)
print(frank.id)
