import requests

api_key = 'd329b7ac-6242-4c5c-b5dd-24c5ea9652a8'
keyword = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{keyword}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)