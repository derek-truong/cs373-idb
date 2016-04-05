# -----------
# Can use this to parse Google Places data
# -----------

# KEYS:
# AIzaSyCEDZvR0eoo1lwHuXAdiYy5wFTq3Qr9uEw Derek
# AIzaSyABe44CFZk2ReG4dCHsSUCNFd6BDZppkOU
# AIzaSyCv_aPVqnNaqdxmnALRLCKaKsn0nhaLynQ
# AIzaSyCZS3L4xfFLxhbsvBXPPPF9v8hBO3SmI-U
# AIzaSyCBObTwMQAkUD5av7E_oUDAZpe-OUkmqfU Julie


import urllib.request, urllib.parse, urllib.error
import json

textserviceurl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

# museums in austin, tx
key = 'AIzaSyCZS3L4xfFLxhbsvBXPPPF9v8hBO3SmI-U'

# create empty list
info_list = []

f = open("Cities.txt",'r')
f = f.read()
cities = f.split('\n')
# cities = ['Hong Kong', 'London', 'Singapore', 'Bangkok', 'Paris', 'Macao', 'Shenzhen', 'New York City', 'Istanbul', 'Kuala Lumpur']
restaurant_id = 0
for c in range(1,len(cities)+1): 
    query = cities[c-1]

    values = {'query' : query+" restaurants", 'key' : key}

    url = textserviceurl + urllib.parse.urlencode(values)

    try:
        data = urllib.request.urlopen(url)
        data = data.read().decode('utf-8')
        saveFile = open('placesdata.txt','w')
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
    while (count < 3) :
        restaurant_id +=1
        name = js['results'][count]['name']
        result = count
        try: 
            rating = js['results'][count]['rating']
        except:
            rating = 'None'

        try :
            category = js['results'][count]['types'][0]
        except :
            category = 'Unknown'

        try :
            address = js['results'][count]['formatted_address']
        except :
            address = 'Unknown'
        try: 
            hours = js['results'][count]['opening_hours']['open_now']
            if hours == True :
                opennow = 'yes'
            else : 
                opennow = 'no'
        except:
            opennow = 'Unknown'
        try: 
            price = js['results'][count]['price_level']
        except:
            price = None

        # print ('result :', result, '\n' 'name: ', name, '\n' 'rating: ', rating, '\n' 'open now: ', opennow)
        # print ('category: ',  category, '\n' 'price level: ', price, '\n' 'address: ', address)
        
        # add to dict instead of print
        info_dict = {'id': restaurant_id,'name': name, 'rating': rating, 'category':  category, 'address': address, "city_id": c}
        info_list.append(info_dict)

        count += 1 

print (info_list)
