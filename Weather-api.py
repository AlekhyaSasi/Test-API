import http.client

conn = http.client.HTTPSConnection("api.weatherapi.com")
payload = ''
headers = {}
conn.request("GET", "/v1/current.json?q=Paris&Key=b21348a9184e494aa0934948212610", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
