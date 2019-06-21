#2 functions 1 for auth and 1 for identity
from user import User
users=[User(1,"jam","mypass"),User(2,"shi","mypasss")]

username_table={u.username:u for u in users}
userid_table={u.id:u for u in users}

def authenticate(username,password):
    #check if user exist
    #if so,return user
    user=username_table.get(username,None)
    if user and password ==user.password:
        return user
#for more concern look flask jwt docs
def identity(payload):
    user_id=payload['identity']
    return userid_table.get(user_id,None)
