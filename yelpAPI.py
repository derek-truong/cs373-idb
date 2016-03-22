from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = Oauth1Authenticator('ITlCwpUMdoFDjqHA5EX5xw', 'VSRV728X6MmtLMxnoGTczyyriBo',
                  'RrKIS5Ot5wUm1oCFd_VX-m9iFy63Gay9', 'vd8tg7pNO8dY5AMwTDgqSQ5cq08')

client = Client(auth)

params = {
    'term': 'food',
    'lang': 'fr'
}

response = client.search('San Francisco', **params)
for x in response.businesses:
	print(x.name)