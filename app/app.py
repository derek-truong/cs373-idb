import logging
import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from models import City, Restaurant, Attraction
from sqlalchemy.orm import sessionmaker, class_mapper
# from sqlalchemy_fulltext import FullText, FullTextSearch

import json
import subprocess

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Welcome to Carina Guestbook")


# SQLALCHEMY_DATABASE_URI = \
#     '{engine}://{username}:{password}@{hostname}/{database}'.format(
#         engine='mysql+pymysql',
#         username=os.getenv('MYSQL_USER'),
#         password=os.getenv('MYSQL_PASSWORD'),
#         hostname=os.getenv('MYSQL_HOST'),
#         database=os.getenv('MYSQL_DATABASE'))
SQLALCHEMY_DATABASE_URI = 'sqlite:///swespt.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)


def reload_data(s,type, file_path):
	with open(file_path) as json_file:
		# print(json_file.read())
		json_str = json_file.read()
		json_data = json.loads(json_str)
		for x in json_data:
			if type == City:
				s.add(type(id=x["id"], name=x["name"].encode('utf8'), country=x["country"], population=x["population"], demonym=x["demonym"], elevation=x["elevation"], description="description", image=x["image"]))
			if type == Attraction:
				s.add(type(id=x["id"], name=x["name"].encode('utf8'), rating=x["rating"], city_id = x["city_id"], num_reviews = x["num_reviews"], category = x["category"], image=x["image"]))
			if type == Restaurant:
				s.add(type(id=x["id"], name=x["name"].encode('utf8'), rating=x["rating"], city_id = x["city_id"], category = x["category"], address=x["address"].encode('utf8'), image=x["image"]))
			s.commit()

def serialize(model): 	
	# """Transforms a model into a dictionary which can be dumped to JSON."""
	columns = [c.key for c in class_mapper(model.__class__).columns]
	return dict((c, getattr(model, c)) for c in columns)

#Splash/Home page
@app.route('/')
@app.route('/home')
def home_page():

	city = db.session.query(City).all()
	attractions = db.session.query(Attraction).all()
	restaurants = db.session.query(Restaurant).all()
	# print("reading correctly")
	return render_template('index.html', cities= city, attractions =attractions, restaurants = restaurants)

#city detail page
@app.route('/cities')
def cities():
	return render_template('cities.html')

#city detail page
@app.route('/cities/<int:city_id>')
def city_detail(city_id):
	city = db.session.query(City).get(city_id)
	print("reading city id in  correctly")
	attractions =db.session.query(Attraction).filter_by(city_id = city_id)
	restaurants =db.session.query(Restaurant).filter_by(city_id = city_id)
	print("reading other shit in  correctly")
	return render_template( 'city.html', city =city, Attractions =attractions, Restaurants = restaurants)

# Restaurants Table
@app.route('/restaurants')
def restaurants():
	return render_template('restaurants.html')

#Restaurant detail page
@app.route('/restaurants/<int:r_id>')
def restaurant_detail(r_id):
	restaurant = db.session.query(Restaurant).get(r_id)
	city = db.session.query(City).get(restaurant.city_id)
	return render_template('restaurant.html',restaurant = restaurant, city = city)

# Attractions Table
@app.route('/attractions')
def attractions():
	return render_template('attractions.html')

@app.route('/attractions/<int:a_id>')
def attraction_detail(a_id):
	attraction = db.session.query(Attraction).filter_by(id=a_id).one()
	city = db.session.query(City).filter_by(id=attraction.city_id).one()
	return render_template('attraction.html',attraction = attraction, city = city)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/recipes')
def recipes():
	return render_template('recipe.html')

@app.route('/tests')
def tests():
	cmd = subprocess.Popen(['make', 'test'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, error = cmd.communicate()
	memory = error.splitlines()
	memory += out.splitlines()

	return render_template('tests.html', memory = memory)

# ######### API ROUTES ###########

#City detail api page
@app.route('/api/cities/<int:city_id>')
def city_detail_api(city_id):
	c = session.query(City).filter_by(id=city_id).one()
	return json.dumps(serialize(c))

#Attraction detail api page
@app.route('/api/attractions/<int:a_id>')
def attraction_detail_api(a_id):
	a = db.session.query(Attraction).filter_by(id=a_id).one()
	return json.dumps(serialize(a))

#Restaurant detail api page
@app.route('/api/restaurants/<int:r_id>')
def restaurant_detail_api(r_id):
	r = db.session.query(Restaurant).filter_by(id=r_id).one()
	return json.dumps(serialize(r))

#Cities api page
@app.route('/api/cities')
def city_api():
	l = []
	for c in db.session.query(City).all() :
		d = serialize(c)
		d["name"] = d["name"].decode('utf8')
		l.append(d)
	return json.dumps(l)

#Attractions api page
@app.route('/api/attractions')
def attraction_api():
	l = []
	for x in db.session.query(Attraction, City).filter(Attraction.city_id == City.id).all():
		d = serialize(x[0])
		d["name"] = d["name"].decode('utf8')
		# print (x)
		d["city_name"] = x[1].name.decode('utf8')
		l.append(d)
	return json.dumps(l)

#Restaurant api page
@app.route('/api/restaurants')
def restaurant_api():
	l = []
	for x in db.session.query(Restaurant, City).filter(Restaurant.city_id == City.id).all():
		d = serialize(x[0])
		d["name"] = d["name"].decode('utf8')
		# print (x)
		d["city_name"] = x[1].name.decode('utf8')
		d["address"] = d["address"].decode('utf8')
		l.append(d)
	return json.dumps(l)

@app.route('/search', methods=['GET'])
def search():
	query = request.args.get('q')
	for x in db.session.query(City).filter(FullTextSearch(query, City)).all() :
		d=serialize(x[0])
		print(d['name'])
	return "hello"
	
@manager.command
def create_db():
	db.create_all()
	reload_data(db.session, City,"Cities.json")
	reload_data(db.session, Attraction, "Attractions.json")
	reload_data(db.session, Restaurant, "Restaurants.json")

@manager.command
def drop_db():
	db.session.query(Attraction).delete()
	db.session.query(Restaurant).delete()
	db.session.query(City).delete()

if __name__ == '__main__':
	logger.debug("Main Method")
	drop_db()
	create_db()
	manager.run()

