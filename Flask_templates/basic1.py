from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    User_logged_in=False
    mylist=[1,2,3,4,5]
    puppies=['rufus','spkie','tune']
    return render_template('basic1.html',mylist=mylist,puppies=puppies,User_logged_in=User_logged_in)

if __name__=='__main__':
    app.run(debug=True)
