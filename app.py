import logging
import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from models import Base, City, Attraction, Restaurant
import dbops
import json
import subprocess

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

@app.route('/tests')
def tests():
	cmd = subprocess.Popen(['make', 'test'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, error = cmd.communicate()
	memory = error.splitlines()
	memory += out.splitlines()

	return render_template('tests.html', memory = memory)

######### API ROUTES ###########


#City detail api page
@app.route('/api/cities/<int:city_id>')
def city_detail_api(city_id):
	c = dbops.db_read(City, city_id)
	return json.dumps(dbops.serialize(c))

#Attraction detail api page
@app.route('/api/attractions/<int:a_id>')
def attraction_detail_api(a_id):
	a = dbops.db_read(Attraction, a_id)
	return json.dumps(dbops.serialize(a))

#Restaurant detail api page
@app.route('/api/restaurants/<int:r_id>')
def restaurant_detail_api(r_id):
	r = dbops.db_read(Restaurant, r_id)
	return json.dumps(dbops.serialize(a))

#Cities api page
@app.route('/api/cities')
def city_api():
	cl = [dbops.serialize(c) for c in dbops.db_read_all(City)]
	return json.dumps(cl)

#Attractions api page
@app.route('/api/attractions')
def attraction_api():
	l = []
	for x in dbops.db_city_join(Attraction):
		d = dbops.serialize(x[0])
		print (x)
		d["city_name"] = x[1].name
		l.append(d)
	return json.dumps(l)

#Restaurant api page
@app.route('/api/restaurants')
def restaurant_api():
	l = []
	for x in dbops.db_city_join(Restaurant):
		d = dbops.serialize(x[0])
		print (x)
		d["city_name"] = x[1].name
		l.append(d)
	return json.dumps(l)



if __name__ == '__main__':
    # manager.run()
    dbops.drop_table(City)
    dbops.drop_table(Attraction)
    dbops.drop_table(Restaurant)
    dbops.reload_data(City,"Cities.json")
    dbops.reload_data(Attraction, "Attractions.json")
    dbops.reload_data(Restaurant, "Restaurants.json")
    app.run()
