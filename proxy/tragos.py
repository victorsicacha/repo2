import requests

class Tragos:
    trago = str(input("introduzca el nombre del trago que quiere buscar"))
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
    print(response.status_code )
    tragos = response.json()["drinks"]
    lista_de_tragos = []
    for i in range(len(tragos)):
        lista_de_tragos.append(tragos[i]["strDrink"])
