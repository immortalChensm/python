import urllib.request
import json


jsonobj = {"name":"tom","age":1000}

with open("file/test.json","w") as f:
    json.dump(jsonobj,f)