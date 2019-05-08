from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index4():
    return render_template('index4.html')

@app.route('/report')
def report():
    username=request.args.get('username')
    lun=False
    ntl=False
    ntlu=False
    ntlun=False
    ntu=False
    ntusername=False
    if any(c.islower() for c in username) and any(c.isupper() for c in username) and username[-1].isdigit():
        lun=True
    elif not any(c.islower() for c in username) and any(c.isupper() for c in username) and username[-1].isdigit():
        ntl=True
    elif not any(c.islower() for c in username) and not any(c.isupper() for c in username) and username[-1].isdigit():
        ntlu=True
    elif not any(c.islower() for c in username) and not any(c.isupper() for c in username) and not username[-1].isdigit():
        ntlun=True
    elif any(c.islower() for c in username) and not any(c.isupper() for c in username) and username[-1].isdigit():
        ntu=True

    return render_template('report.html',username=username,lun=lun,ntl=ntl,ntlu=ntlu,ntlun=ntlun,ntu=ntu)


if __name__=='__main__':
    app.run(debug=True)
