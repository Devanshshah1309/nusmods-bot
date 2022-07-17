import requests
URL = "http://api.nusmods.com/v2/2022-2023/modules/"

def getModuleDescription(module_code: str):
    r = requests.get(f"{URL}{module_code}.json")
    if r.status_code != 200:
        return "Sorry module not found! Please ensure that you have entered the correct module code"
    data = r.json()
    return data['description']