#Using HTTP Client
import http.client
import pprint
import json

conn = http.client.HTTPSConnection("api.weatherapi.com")
payload = ''
headers = {}
conn.request("GET",
             "/v1/current.json?q=Paris&Key=b21348a9184e494aa0934948212610",
             payload, headers)
response = conn.getresponse()
data = response.read()
pretty_json = json.loads(data)
pprint.pprint(pretty_json)
