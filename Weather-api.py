import http.client

conn = http.client.HTTPSConnection("api.weatherapi.com")
headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

conn.request("GET", "/ip.json?q=%3CREQUIRED%3E", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
