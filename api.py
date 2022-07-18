import requests
URL = "http://api.nusmods.com/v2/2022-2023/modules/"
"""
Returns the relevant info about the module. If no info is specified, returns all the details.
Possible values of info are:
1. acadYear
2. preclusion
3. description
4. title
5. department
6. faculty
7. prerequisite
8. moduleCredit
9. moduleCode
10. semesterData
"""
def getModuleDetails(module_code: str, info = None):
    r = requests.get(f"{URL}{module_code}.json")
    if r.status_code != 200:
        return "Sorry module not found! Please ensure that you have entered the correct module code"
    data = r.json()
    if info == None:
        return data
    result = data.get(info)
    if result == None:
        return f"Sorry, there does not appear to be any {info} for {module_code}"
    return result

def getModuleDescription(module_code: str):
    return getModuleDetails(module_code, info="description")

def getModulePrerequisite(module_code: str):
    return getModuleDetails(module_code, info="prerequisite")

