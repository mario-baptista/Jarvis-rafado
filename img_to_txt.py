import requests
from bs4 import BeautifulSoup

url = "https://ocrly-image-to-text.p.rapidapi.com/"

querystring = {"filename":"sample.jpg","imageurl":"https://i.pinimg.com/originals/42/1b/e6/421be6184e75937bb223c764ecbc2f2e.jpg"}

headers = {
    'x-rapidapi-key': "d2072b6a7amshfc3757b6b6be6f0p1d4a12jsna54f7c9d1127",
    'x-rapidapi-host': "ocrly-image-to-text.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
html = response.text
soup = BeautifulSoup(html)
print(soup.get_text())