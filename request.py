import requests


url = 'http://localhost:5000/api'
r = requests.post(url,json={'gender':1, 'married':0, 'education':1})
print(r.json())
