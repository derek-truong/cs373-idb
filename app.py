import logging
import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
manager = Manager(app)


#Splash/Home page
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('index.html')

#city detail page
@app.route('/cities')
def cities():
	return render_template('cities.html')

#city detail page
@app.route('/cities/<int:city_id>')
def city_detail(city_id):
	city_pages = ['LA', 'barcelona', 'prague']
	return render_template(city_pages[city_id] + '.html')


# Restaurants Table
@app.route('/restaurants')
def restaurants():
	return render_template('restaurants.html')

#Restaurant detail page
@app.route('/restaurants/<int:r_id>')
def restaurant_detail(r_id):
	r_pages = ['eggslut', 'cera-23','den-noc']
	return render_template(r_pages[r_id] + '.html')

# Attractions Table
@app.route('/attractions')
def attractions():
	return render_template('attractions.html')



@app.route('/attractions/<int:a_id>')
def attraction_detail(a_id):
	a_pages = ['urban-light','basilica', 'charles-bridge']
	return render_template(a_pages[a_id] + '.html')



@app.route('/about')
def about():
	return render_template('about.html')





if __name__ == '__main__':
    manager.run()