# -----------
# Can use this to parse Google Places data
# -----------
# https://github.com/Yelp/yelp-python/blob/4a8bea62cd337085f86dcc75d3f58f7f92a09234/README.md
# https://github.com/Yelp/yelp-python/blob/4a8bea62cd337085f86dcc75d3f58f7f92a09234/yelp/endpoint/search.py

import urllib.request, urllib.parse, urllib.error
import json, io
import calendar, time
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key= "8e59B-StCRN4EjpxmNF6FQ",
    consumer_secret= "rSWcfqXl66yYIgkPioh0PlCqHjM",
    token= "RJMSPeTXZxjQ49f94xpx-QhtLIJN9ITv",
    token_secret="X96YifgDJFZxEOReeUh1_m0PqXU"
)

client = Client(auth)

with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)


# wikiserviceurl = 'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json?'
yelpserviceurl = 'https://api.yelp.com/v2/search/?'
# key = 'AIzaSyCBObTwMQAkUD5av7E_oUDAZpe-OUkmqfU' # for googleapi

cities = ['Hong Kong', 'London', 'Singapore', 'Bangkok', 'Paris', 'Macao', 'Shenzhen', 'New York City', 'Istanbul', 'Kuala Lumpur']
results = []

for c in cities: 
    city = c

    # values = {'query' : query, 'key' : key}
    values = {'term': 'restaurant', 'location' : city}

    # client.search(city, **values)

    url = yelpserviceurl + urllib.parse.urlencode(values)

    try:
        data = urllib.request.urlopen(url)
        data = data.read().decode('utf-8')
        saveFile = open('citiesdata.txt','w')
        saveFile.write(str(data))
        saveFile.close()
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        continue


    try: 
        js = json.loads(str(data))
    except: 
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    count = 0
    while count < len(js['businesses'] or count < 50) :
        result = count
        name = js['businesses'][count]['name']
        try:
            location = js['businesses'][count]['location']['city']
        except:
            location = 'Not found'
        try: 
            rating = js['businesses'][count]['rating']
        except:
            rating = 'None'
        try :
            category = js['businesses'][count]['categories'][0]
        except :
            category = 'Unknown'
        try :
            address = js['businesses'][count]['address']
        except :
            address = 'Unknown'
        # try: 
        #     hours = js['results'][count]['opening_hours']['open_now']
        #     if hours == True :
        #         opennow = 'yes'
        #     else : 
        #         opennow = 'no'
        # except:
        #     opennow = 'Unknown'
        # try: 
        #     price = js['results'][count]['price_level']
        # except:
        #     price = None

        print ('result: ', result, '\n' 'name: ', name, '\n' 'location: ', location, '\n', 'rating: ', rating)
        # , '\n' 'open now: ', opennow)
        print ('category: ', category, '\n' 'address: ', address)
        # print ('type: ',  placetype, '\n' 'price level: ', price, '\n' 'address: ', address)
        
        # info = {
        #     "name":    name,
        #     "location": location,
        #     "rating":  rating,
        #     "category": category,
        #     "address": address
        # }
        # results.append(info)

        count += 1 
