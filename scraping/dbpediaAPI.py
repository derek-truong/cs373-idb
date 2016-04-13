import urllib, json
from urllib.request import urlopen
from pprint import pprint


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

f = open("dbpedia_cities.txt",'r')
f = f.read()
f = f.split('\n')

g = open("Cities.txt",'r')
g = g.read()
g = g.split('\n')

cities = []

for x in range(len(f)) :
	url = "http://dbpedia.org/data/" + f[x] + ".json"
	response = urlopen(url).read().decode('utf8')
	obj = json.loads(response)
	attributes = []
	json_url = "http://dbpedia.org/resource/" + f[x]

	population = "NULL"
	country = "NULL"
	demonym = "NULL"
	elevation = "NULL"
	description = "NULL"

	city_id = x+1
	#print(city_id)
	
	name = g[x]
	name = name.replace("_"," ")
	#print(name)

	if "http://dbpedia.org/property/populationBlank" in obj[json_url] :
		if RepresentsInt(obj[json_url]["http://dbpedia.org/property/populationBlank"][0]["value"]) :
			population = obj[json_url]["http://dbpedia.org/property/populationBlank"][0]["value"]
	if "http://dbpedia.org/ontology/populationTotal" in obj[json_url] :
		population = obj[json_url]["http://dbpedia.org/ontology/populationTotal"][0]["value"]
	elif "http://dbpedia.org/property/populationMetro" in obj[json_url] :
		population = obj[json_url]["http://dbpedia.org/property/populationMetro"][0]["value"]
	
	try:
		population = int(population)
	except ValueError:
		population = "Null"


	if "http://dbpedia.org/ontology/country" in obj[json_url] :
		country = obj[json_url]["http://dbpedia.org/ontology/country"][0]["value"]
	elif "http://dbpedia.org/property/membership" in obj[json_url] :
		country = obj[json_url]["http://dbpedia.org/property/membership"][0]["value"]		
	country = country.split('/')
	country = country[-1]
	country = country.replace('_'," ")

	if "http://dbpedia.org/property/populationBlank" in obj[json_url] :
		for x in range(len(obj[json_url]["http://dbpedia.org/property/populationBlank"])) :
			if not RepresentsInt(obj[json_url]["http://dbpedia.org/property/populationBlank"][x]["value"]) :
				demonym = obj[json_url]["http://dbpedia.org/property/populationBlank"][x]["value"]	
	if "http://dbpedia.org/property/populationDemonym" in obj[json_url] :
		demonym = obj[json_url]["http://dbpedia.org/property/populationDemonym"][0]["value"]
	elif "http://dbpedia.org/property/demonym" in obj[json_url] :
		demonym = obj[json_url]["http://dbpedia.org/property/demonym"][0]["value"]
	elif "http://dbpedia.org/property/free" in obj[json_url] :
		demonym = obj[json_url]["http://dbpedia.org/property/free"][2]["value"]
	
	demonym = demonym.split('/')
	demonym = demonym[-1]
	country.replace('_',' ')

	if "http://dbpedia.org/ontology/elevation" in obj[json_url] :
		elevation = obj[json_url]["http://dbpedia.org/ontology/elevation"][0]["value"]
	elif "http://dbpedia.org/ontology/maximumElevation" in obj[json_url] :
		elevation = obj[json_url]["http://dbpedia.org/ontology/maximumElevation"][0]["value"]
	elif "http://dbpedia.org/property/elevationMaxM" in obj[json_url] :
		elevation = obj[json_url]["http://dbpedia.org/property/elevationMaxM"][0]["value"]
	elif "http://dbpedia.org/property/elevationFt" in obj[json_url] :
		elevation = int(obj[json_url]["http://dbpedia.org/property/elevationFt"][0]["value"])*.3048
	elif "http://dbpedia.org/property/parts" in obj[json_url] :
		elevation = obj[json_url]["http://dbpedia.org/property/parts"][0]["value"]
	
	try:
		elevation = float(elevation)
	except ValueError:
		elevation = "Null"

	d = obj[json_url]["http://www.w3.org/2000/01/rdf-schema#comment"]
	description = ""
	for i in range(len(d)) :
		if d[i]["lang"] == "en" :
			description = d[i]["value"]
	

	temp_city = {"id": city_id,"name":name,"population": population, "country": country, "demonym": demonym, "elevation": elevation}
	cities.append(temp_city)
	
print(cities)

# Cambridge Demonym = Cantabrigian
# Cambridge Population = 123,867 
# Hong Kong Elevation = 429
# Lyon Demonym = Lyonese, Lyonnais
# Paris Elevation = 35
# Prague Demonym = Praguer
# Puerto Rico Elevation = 1338
# Queenstown Elevation = 310
# Queenstown Population = 28,224
# Seattle Country = United States
# Sydney Demonym = Sydneysider
# Sydney Elevation = 19
# Vatican City Country = Vatican City
# Vatican City Elevation = 76.2
# Yokohama Country = Japan
# Yokohama Elevation = 43