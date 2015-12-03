import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Orders, Base
import stripe

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}
stripe.api_key = stripe_keys['secret_key']

engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()
app = Flask(__name__)
price = 86
@app.route('/')
def welcomePage():
  return render_template('index.html')

@app.route('/cart', methods=['GET', 'POST'])
@app.route('/cart/', methods=['GET', 'POST']) 
def newOrder():
	if request.method == 'POST':
	    newOrder = Orders(count =request.form['count'], name = request.form['name'], address = request.form['address'], email = request.form['email'])
	    session.add(newOrder)
	    session.commit()
	    return redirect(url_for('charge'))
	else:
	    return render_template('cart.html', price = price, key=stripe_keys['publishable_key'])

@app.route('/charge', methods=['GET', 'POST'])
def charge():
		return render_template('charge.html')

    # # Amount in cents
    # amount = 500
    # It is for new customer 
    # customer = stripe.Customer.create(
    #     email='customer@example.com',
    #     card=request.form['stripeToken']
    # )

    # charge = stripe.Charge.create(
    #     customer=customer.id,
    #     amount=amount,
    #     currency='usd',
    #     description='Flask Charge'
    # )
    # For other customers leave only return statment


if __name__ =='__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True # reload if see any code changes
  app.run(host = '0.0.0.0', port = 8080)