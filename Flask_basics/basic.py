from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return "<h1> Hello puppy</h1>"

@app.route('/information')
def info():
    return "<h1> Puppies are  cute</h1>"
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>Some Name Some Index {}</h1>".format(name[1])
    # return "<h1> Upper Case: {}</h1>".format(name.upper())
    # return "<h1>this is a page for {}</h1>".format(name)
@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name[-1]=='y':
        name=name[:-1]+"iful"
    else:
        name=name+'y'
    return "<h1>Your puppy_latin name is :  {}</h1>".format(name)


if __name__=='__main__':
    app.run(debug=True)
