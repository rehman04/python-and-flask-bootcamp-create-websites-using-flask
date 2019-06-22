from flask import Flask, render_template, request,redirect,url_for
import stripe

app=Flask(__name__)

#example keys
public_key="pk_test_TYooMQauvdEDq54NiTphI7jx"
stripe.api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"

@app.route("/")
def index():
    return render_template("index.html",public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment',methods=['POST'])
def payment():
    #customer info
    customer=stripe.Customer.create(email=request.form['stripeEmail'],
                                    source=request.form['stripeToken'])
    #payment info
    charge=stripe.Charge.create(
            customer=customer.id,
            amount=1999,
            currency='usd',
            description='Donation'
    )
    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)
