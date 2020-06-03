import urllib.request

import json

jsonpath = "file/menu.json"
with open(jsonpath,"rb") as f:
    jsondata = json.load(f)
    print(jsondata)
    print(type(jsondata))