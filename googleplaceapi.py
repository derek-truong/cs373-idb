# -----------
# Can use this to parse Google Places data
# -----------

import urllib.request, urllib.parse, urllib.error
import json

textserviceurl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

# museums in austin, tx
key = 'AIzaSyCBObTwMQAkUD5av7E_oUDAZpe-OUkmqfU'

while True:
    query = input('Enter query: ')
    if len(query) < 1 : query = 'tourist attractions in barcelona'

    values = {'query' : query, 'key' : key}

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
    while count < len(js['results'] or count < 50) :
        name = js['results'][count]['name']
        result = count+1
        try: 
            rating = js['results'][count]['rating']
        except:
            rating = 'None'

        try :
            placetype = js['results'][count]['types'][0]
        except :
            placetype = 'Unknown'

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

        print ('result :', result, '\n' 'name: ', name, '\n' 'rating: ', rating, '\n' 'open now: ', opennow)
        print ('type: ',  placetype, '\n' 'price level: ', price, '\n' 'address: ', address)
        
        count += 1 
