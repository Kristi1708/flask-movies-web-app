import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-key': "754bf32cb9msh1da68a05c8eff47p14144bjsnd886ba44cc4f",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data=response.json()
print(data)