#Using HTTP Client
import http.client
import pprint
import json

conn = http.client.HTTPSConnection("api.weatherapi.com")
payload = ''
headers = {}
conn.request("GET",
             "/v1/current.json?q=Paris&Key={{api_key}}",
             payload, headers)
response = conn.getresponse()
data = response.read()
pretty_json = json.loads(data)
pprint.pprint(pretty_json)

# Using request library

import requests
from pprint import pprint
params = {'q' : 'Paris',
'key' : 'api_key'}
url = "http://api.weatherapi.com/v1/current.json"

try:
  response = requests.get(url, params =params, timeout=5)
  response.raise_for_status()
  pprint (response.json())
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

