import http.client

conn = http.client.HTTPSConnection("api.weatherapi.com")
payload = ''
headers = {}

conn.request("GET", "/v1/current.json?q=Paris&Key={{YOURKEY}}", payload, headers)
response = conn.getresponse()
data = response.read()
print(data.decode("utf-8"))
