from flask import Flask, render_template, request, redirect, url_for, flash, jsonify    
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Orders, Base

engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()
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
	    return redirect(url_for('welcomePage'))
	else:
	    return render_template('cart.html', price = price)

if __name__ =='__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True # reload if see any code changes
  app.run(host = '0.0.0.0', port = 8080)