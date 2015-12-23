# About BuyTests
  This is an e-commerce website built using Stripe API for web payments
  This application is for infertility clinic in Russia. Content written 
  in Russian. 

# Getting Started

1. Install Vagrant and VirtualBox
2. Install software listed in requirements
3. Clone the BuyTests repository
4. In terminal navigate to BuyTests directory
5. Type the command to run VM: vagrant up
6. Type the commant to log into VM: vagrant ssh
7. Run application within the VM:
 - python database_setup.py
 - python orders.py
8. Access and test your application by visiting http://localhost:8080 locally

# Requirements
 - Python 3.0
 - Werkzeug 0.8.3
 - Flask 0.9
 - Flask-Login 0.1.3
 - SQLAlchemy 0.8.4
