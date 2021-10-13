import requests

# op = int(input("0 - URL\n1 - Local (img/img.jpg)\n"))
op = 1

if op == 0:
    url = input("URL: ")
    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        data={
            'image': url,
        },
        headers={'api-key': 'c78951d6-4e75-4ed6-bdac-1b67985d40ce'}
    )
    print(r.json())

else:
    import requests
    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open('discord bot/img.png', 'rb'),
        },
        headers={'api-key': 'c78951d6-4e75-4ed6-bdac-1b67985d40ce'}
    )
    print(r.json())