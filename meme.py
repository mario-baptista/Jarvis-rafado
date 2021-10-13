import requests
import json
from PIL import Image
import webbrowser

r = requests.get('https://meme-api.herokuapp.com/gimme')

url = r.json()["url"]

if url.endswith(".gif"):
    webbrowser.open(url)
else:
    im = Image.open(requests.get(url, stream=True).raw)
    im.show()
print(url)