
import requests
import os
import sys
url = "http://hospital.mppstore.com/api/trains/test"
data = {
    "name":"tom",
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ob3NwaXRhbC5tcHBzdG9yZS5jb21cL2FwaVwvbG9naW4iLCJpYXQiOjE1MzY1ODUxMTksImV4cCI6MTUzNjU4ODcxOSwibmJmIjoxNTM2NTg1MTE5LCJqdGkiOiJHV1J6akNYSFVWV2NTNmM0Iiwic3ViIjo1MSwicHJ2IjoiYzgzZTZhZTllYTM2OGIxMTVmMjMxMzQyN2Y1ZDVjMGY5ZDEzYzc2MyJ9.0lhcyf8ZCQO7dwTftC0x3Pap17jl_p7KO0NsqmfbjKw"
}
result = requests.post(url,data=data)
print(result.text)

print(sys.__doc__)