import http.client

conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "cb5a72895amshfe4c9b910ff10eep137693jsnf0f1a383cda0",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

conn.request("GET", "/country/code?code=it", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))