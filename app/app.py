import logging
import os

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from models import City, Restaurant, Attraction
from sqlalchemy.orm import sessionmaker, class_mapper
from sqlalchemy import or_, and_
import json
import subprocess

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


# SQLALCHEMY_DATABASE_URI = \
#     '{engine}://{username}:{password}@{hostname}/{database}'.format(
#         engine='mysql+pymysql',
#         username=os.getenv('MYSQL_USER'),
#         password=os.getenv('MYSQL_PASSWORD'),
#         hostname=os.getenv('MYSQL_HOST'),
#         database=os.getenv('MYSQL_DATABASE'))

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://travis:@localhost/test?charset=utf8'

SQLALCHEMY_DATABASE_URI = 'sqlite:///swespt.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
db = SQLAlchemy(app)


# def reload_data(s,type, file_path):
# 	with open(file_path) as json_file:
# 		json_str = json_file.read()
# 		json_data = json.loads(json_str)
# 		for x in json_data:
# 			if type == City:
# 				s.add(type(id=x["id"], name=x["name"].encode('utf8'), country=x["country"], population=x["population"], demonym=x["demonym"], elevation=x["elevation"], description=x["description"].encode('utf8'), image=x["image"]))
# 			if type == Attraction:
# 				s.add(type(id=x["id"], name=x["name"].encode('utf8'), rating=x["rating"], city_id = x["city_id"], num_reviews = x["num_reviews"], category = x["category"], image=x["image"]))
# 			if type == Restaurant:
# 				s.add(type(id=x["id"], name=x["name"].encode('utf8'), rating=x["rating"], city_id = x["city_id"], category = x["category"], address=x["address"].encode('utf8'), image=x["image"]))
# 		s.commit()

def reload_data(s,type, file_path):
	with open(file_path, encoding = "utf8") as json_file:
		# print(json_file.read())
		json_str = json_file.read()
		json_data = json.loads(json_str)
		for x in json_data:
			s.add(type(**x))
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
	c = db.session.query(City).filter_by(id=city_id).one()
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
	cl = [serialize(c) for c in db.session.query(City).all()]
	return json.dumps(cl)

#Attractions api page
@app.route('/api/attractions')
def attraction_api():
	l = []
	for x in db.session.query(Attraction, City).filter(Attraction.city_id == City.id).all():
		d = serialize(x[0])
		print (x)
		d["city_name"] = x[1].name
		l.append(d)
	return json.dumps(l)

#Restaurant api page
@app.route('/api/restaurants')
def restaurant_api():
	l = []
	for x in db.session.query(Restaurant, City).filter(Restaurant.city_id == City.id).all():
		d = serialize(x[0])
		print (x)
		d["city_name"] = x[1].name
		l.append(d)
	return json.dumps(l)

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route('/api/search', methods=['GET'])
def search_api():
	query_str = request.args.get('q')
	words = query_str.split(' ')
	ol = []
	al = []

	# Handles the OR Clauses
	c = db.session.query(City).filter(or_(*[or_(City.id.contains(w), City.name.contains(w),
		City.population.contains(w), City.country.contains(w), City.demonym.contains(w),
		City.elevation.contains(w)) for w in words])).all()
	a = db.session.query(Attraction).filter(or_(*[or_(Attraction.id.contains(w),
		Attraction.name.contains(w), Attraction.rating.contains(w), Attraction.city_id.contains(w),
		Attraction.num_reviews.contains(w), Attraction.category.contains(w)) for w in words])).all()
	r = db.session.query(Restaurant).filter(or_(*[or_(Restaurant.id.contains(w),
		Restaurant.name.contains(w), Restaurant.rating.contains(w), Restaurant.city_id.contains(w),
		Restaurant.category.contains(w), Restaurant.address.contains(w)) for w in words])).all()

	# Handles the AND Clauses
	ca = db.session.query(City).filter(and_(*[or_(City.id.contains(w), City.name.contains(w),
		City.population.contains(w), City.country.contains(w), City.demonym.contains(w),
		City.elevation.contains(w)) for w in words]))
	aa = db.session.query(Attraction).filter(and_(*[or_(Attraction.id.contains(w),
		Attraction.name.contains(w), Attraction.rating.contains(w), Attraction.city_id.contains(w),
		Attraction.num_reviews.contains(w), Attraction.category.contains(w)) for w in words])).all()
	ra = db.session.query(Restaurant).filter(and_(*[or_(Restaurant.id.contains(w),
		Restaurant.name.contains(w), Restaurant.rating.contains(w), Restaurant.city_id.contains(w),
		Restaurant.category.contains(w), Restaurant.address.contains(w)) for w in words])).all()

	for x in c:
		ol.append({"name":x.name, "description":"Country: "+x.country,"address":"", "link":"/cities/"+str(x.id)})
	for y in a:
		ol.append({"name":y.name, "description":"Category: "+y.category,"address":"", "link":"/attractions/"+str(y.id)})
	for z in r:
		ol.append({"name":z.name, "description":"Category: "+z.category,"address":"Address: "+z.address, "link":"/restaurants/"+str(z.id)})

	for m in ca:
		al.append({"name":m.name, "description":"Country: "+m.country,"address":"", "link":"/cities/"+str(m.id)})
	for n in aa:
		al.append({"name":n.name, "description":"Category: "+n.category,"address":"", "link":"/attractions/"+str(n.id)})
	for o in ra:
		al.append({"name":o.name, "description":"Category: "+o.category,"address":"Address: "+z.address, "link":"/restaurants/"+str(o.id)})


	wl = {"or_results":ol, "and_results":al}
	return json.dumps(wl)

@manager.command
def create_db():
	db.create_all()
	reload_data(db.session, City,"Cities.json")
	reload_data(db.session, Attraction, "Attractions.json")
	reload_data(db.session, Restaurant, "Restaurants.json")

@manager.command
def drop_db():
	db.session.query(Restaurant).delete()
	db.session.query(Attraction).delete()
	db.session.query(City).delete()

if __name__ == '__main__':
	manager.run()

