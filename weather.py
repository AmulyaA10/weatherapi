mport requests
import json

url = "https://open-weather13.p.rapidapi.com/city"

querystring = {"city":"Dallas","lang":"EN"}

headers = {
  "x-rapidapi-key": "2e3186bb1emsh173af87ec363d8ep1332b3jsn84d96973212d",
  "x-rapidapi-host": "open-weather13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(json.dumps(response.json(),indent=4))
