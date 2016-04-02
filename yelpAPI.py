from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from models import Restaurant, Attraction
from dbops import db_create, db_read, db_read_all
import re

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = Oauth1Authenticator('ITlCwpUMdoFDjqHA5EX5xw', 'VSRV728X6MmtLMxnoGTczyyriBo',
                  'RrKIS5Ot5wUm1oCFd_VX-m9iFy63Gay9', 'vd8tg7pNO8dY5AMwTDgqSQ5cq08')

client = Client(auth)

f = open("Cities.txt",'r')
f = f.read()
f = f.split('\n')

def get_restaurants():
	params = {
	    'term': 'restaurants',
	    'lang': 'en',
	    'limit': 3
	}

	id_num = 0
	city_id = 0
	restaurants = {}
	
	for cities in f:
		city = re.sub("_", " ", cities)
		response = client.search(city, **params)

		for x in response.businesses:
			restaurant = {"id": id_num, "name": x.name, "rating": x.rating, "categ": x.categories[0][0],
			  	 "address": x.location.display_address[0], "city_id": city_id
			}

			restaurants[id_num] = restaurant
			#db_create(Restaurant(**restaurant))
			print(restaurants[id_num]['name'])	
			id_num += 1
		city_id +=1


def get_attractions():
	params = {
	    'term': 'amusement parks',
	    'lang': 'en',
	    'limit': 3
	}

	id_num = 0
	city_id = 0
	attractions = {}

	for cities in f:
		city = re.sub("_", " ", cities)
		response = client.search(city, **params)

		for x in response.businesses:
			attraction = {"id": id_num, "name": x.name, "rating": x.rating, "categ": x.categories[0][0],
			  	 "num_rating": x.review_count, "lat": x.location.coordinate.latitude,
			  	 "lon": x.location.coordinate.longitude,  "city_id": city_id 
			}

			attractions[id_num] = attraction
			#db_create(Attraction(**attraction))
			print(attractions[id_num]['name'])
			id_num += 1
		city_id += 1

get_restaurants()
get_attractions()


