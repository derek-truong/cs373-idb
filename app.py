import logging
import os

from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response, abort, Response
from flask.ext.cors import CORS, cross_origin
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
    city= dbops.db_read_all(City)
    attractions =dbops.db_read_all(Attraction)
    restaurants = dbops.db_read_all(Restaurant)
    print("reading correctly")
    return render_template('index.html', cities= city, attractions =attractions, restaurants = restaurants)

#search
@app.route('/search',  methods=['GET'])
def search():
    query = request.args.get('q')
    page = request.args.get('page')
    searchType = request.args.get('searchType')
    return render_template('search.html', query=query, page=page, searchType=searchType)

#city detail page
@app.route('/cities')
def cities():
    return render_template('cities.html')

#city detail page
@app.route('/cities/<int:city_id>')
def city_detail(city_id):
    city = dbops.db_read(City, city_id)
    print("reading city id in  correctly")
    Attractions =dbops.db_read_city_spots(Attraction, city_id)
    Restaurants =dbops.db_read_city_spots(Restaurant, city_id)
    print("reading other shit in  correctly")
    return render_template( 'city.html',city =city, Attractions =Attractions, Restaurants = Restaurants)

# Restaurants Table
@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

#Restaurant detail page
@app.route('/restaurants/<int:r_id>')
def restaurant_detail(r_id):
    restaurant = dbops.db_read(Restaurant, r_id)
    city = dbops.db_read(City, restaurant.city_id)
    return render_template('restaurant.html',restaurant = restaurant, city = city)

# Attractions Table
@app.route('/attractions')
def attractions():
    return render_template('attractions.html')

@app.route('/attractions/<int:a_id>')
def attraction_detail(a_id):
    attraction = dbops.db_read(Attraction, a_id)
    city = dbops.db_read(City, attraction.city_id)
    return render_template('attraction.html',attraction = attraction, city = city)


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


@app.errorhandler(404)
def page_not_found(e):
    print(40404040040404040404040404044040)
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    print(5000000000000005000000000)
    return render_template('500.html'), 500


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
