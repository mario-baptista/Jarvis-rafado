import requests
from termcolor import colored

print("0 - tv")
print("1 - movie")

a = int(input("Opcao: "))
aux = ""

if a == 0:
    aux = "tv"
elif a == 1:
    aux = "movie"
else:
    exit()
# aux = "tv"
# aux = "movie"

r = requests.get("https://api.themoviedb.org/3/trending/" + aux + "/week?api_key=39fd0ac1dcd7e7a870517b45eb95f3cc")

for movie in r.json()["results"]:
    try: 
        if aux == "movie":
            titulo = movie["title"] + " (" + movie["original_title"] + ")"
            print(colored(titulo, 'cyan'))
        else:
            titulo = movie["name"] + " (" + movie["original_name"] + ")"
            print(colored(titulo, 'cyan'))
    except:
        pass
    try:
        print(movie["overview"])
    except:
        print("erro a obter o resumo do filme")