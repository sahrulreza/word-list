import requests

api_key = "1b0043b3-a3ea-4ef1-96a5-d72c9b288f85"
word = "potato"
url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

res = requests.get(url)

definitions = res.json()


print(definitions)