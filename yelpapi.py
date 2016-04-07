from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
# from models import Restaurant, Attraction
# from dbops import db_create, db_read, db_read_all, db_delete

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = Oauth1Authenticator('ITlCwpUMdoFDjqHA5EX5xw', 'VSRV728X6MmtLMxnoGTczyyriBo',
                  'RrKIS5Ot5wUm1oCFd_VX-m9iFy63Gay9', 'vd8tg7pNO8dY5AMwTDgqSQ5cq08')

client = Client(auth)

f = open("Cities.txt",'r')
f = f.read()
cities = f.split('\n')

# cities = {0: "London", 1: "Austin", 2: "Barcelona", 3: "Paris", 4: "Sydeny", 5: "New York City", 6: "Maui", 7: "Rio de Janeiro", 8: "Houston", 9: "San Francisco", 10: "Dallas", 11: "Prague", 12: "Yellowstone", 13: "Los Angeles", 14: "Vancouver", 15: "Washington D.C", 16: "U.S. Virgin Islands", 17: "Zurich", 18: "Orlando", 19: "Las Vegas", 20: "Berlin", 21: "Crete", 22: "Playa del Carmen", 23: "Puerto Rico", 24: "Rome" }

# def get_restaurants():
# 	params = {
# 	    'term': 'restaurants',
# 	    'lang': 'en',
# 	    'limit': 3
# 	}

# 	id_num = 0
# 	restaurants = {}
# 	for i in range(0, 50):
# 		response = client.search(cities[i], **params)
# 		print(cities[i])

# 		for x in response.businesses:
# 			#dictionary of name, rating, num of ratings, address, and categories
# 			restaurant = {"id": id_num, "name": x.name, "rating": x.rating, "categ": x.categories[0][0],
# 			  	 "address": x.location.display_address[0], "city_id": id_num
# 			}

# 			restaurants[id_num] = restaurant
# 			#db_create(Restaurant(**restaurant))
# 			print(restaurants[id_num]['name'])
# 			id_num += 1

def get_attractions():
	params = {
	    'term': 'attractions',
	    'lang': 'en',
	    'limit': 3
	}

	id_num = 1
	attractions = []
	for w in range(1,len(cities)+1) :
		response = client.search(cities[w-1], **params)

		for x in response.businesses:
			#dictionary of name, rating, num of ratings, address, and categories
			attraction = {"attraction_id": id_num, "name": x.name, "rating": x.rating, "categeory": x.categories[0][0],
			  	 "num_rating": x.review_count, "city_id": w
			}

			attractions.append(attraction)
			#db_create(Attraction(**attraction))
			# print(attractions[id_num])
			id_num += 1
	print(attractions)
get_attractions()





