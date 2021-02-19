
import http.client

conn = http.client.HTTPSConnection("covid-19-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "cb5a72895amshfe4c9b910ff10eep137693jsnf0f1a383cda0",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

conn.request("GET", "/report/totals?date=2020-07-21", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))