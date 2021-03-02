import requests

class Proxy:
    def __init__(self, instance):
        self.instance = instance

    def proxy(self):
        object_instance = self.instance
        trago = object_instance.trago
        path = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
        response = requests.get(f"{path}{trago}")

        if response.status_code == 200 :
            message1 = "aquí le mostraremos un json completo "
            message2 = "de cada trago en nuestra "
            message3 = "base de datos quie tenga que ver con su selección"
            print(f"{message1}{message2}{message3}")
            
            print(
            response.json()
            )
            return True
        return False
