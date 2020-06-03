import urllib.request
import ssl
import urllib.parse
import json
#url = "http://114.118.4.4/rest/n/feed/hot?app=0&lon=120.731163&did_gt=1529111948644&c=MYAPP_CPD&sys=ANDROID_4.4.4&mod=OPPO%28OPPO%20R7%29&did=ANDROID_c0b9408dcd8581d1&ver=5.7&net=WIFI&country_code=cn&iuid=Dur6xzkctMkMUXqx3vZtWDZ2LWa2HFZ9L5qvfDOfF6nqblqgEpNaMcGoOVSJyollFbuQbPd681DtsG%2BNRsCVk6DA&appver=5.7.4.6246&max_memory=256&oc=MYAPP_CPD&ftt=&ud=849970873&language=zh-cn&lat=31.240251"
url = "http://114.118.4.4/rest/n/clc/show?app=0&lon=120.731155&did_gt=1529111948644&priorityType=1&c=MYAPP_CPD&sys=ANDROID_4.4.4&mod=OPPO%28OPPO%20R7%29&did=ANDROID_c0b9408dcd8581d1&ver=5.7&net=WIFI&country_code=cn&iuid=Dur6xzkctMkMUXqx3vZtWDZ2LWa2HFZ9L5qvfDOfF6nqblqgEpNaMcGoOVSJyollFbuQbPd681DtsG%2BNRsCVk6DA&appver=5.7.4.6246&max_memory=256&oc=MYAPP_CPD&ftt=&ud=849970873&language=zh-cn&lat=31.240242"
postData = {
    "log":"CrIECIfg1MzGvc6iFhJQCAEQt/SAJBiUqqXanIDArUgqGzFfaS8xNjA0NzUyNTI5NzczODk5NzgzX2g4MDAsOAFYW2IHNjQweDY0MGoRV0VCUF9TSU1QTEVfUVkyNjUSNAgBEMW8uMcBGN/F2IqXgICBSCocMV9pLzE2MDQ3NTI1Mjk3NzM4OTk3ODNfaDE5MTAtOAISUQgBEIeD0qwBGLWkkoyXgICdSCobMV9hLzE2MDQ3NTI1Mjk3NzM4OTk3ODNfaDg4MC44AVggYgczNjB4NjQwahFXRUJQX1NJTVBMRV9RWTI2NRJSCAEQmujxxAMY+ef05ZyAgMxIKhwxX2EvMTYwNDc1MjUyOTc3Mzg5OTc4M19oMTkwMC84AlhNYgczNjB4NjQwahFXRUJQX1NJTVBMRV9RWTI2NRJQCAEQ7JTaYRif16DDkYDAqEgqGzFfaS8xNjA0NzUyNTI5NzczODk5NzgzX2g2MzAwOAFYKWIHMzYweDY0MGoRV0VCUF9TSU1QTEVfUVkyNjUSUQgBELv/u7wCGOzQ5ZafgIDcSCobMV9pLzE2MDQ3NTI1Mjk3NzM4OTk3ODNfaDg4MDE4AlgxYgczNjB4NjQwahFXRUJQX1NJTVBMRV9RWTI2NRJSCAEQsYbm1QMYzs+f1ZCAwPZIKhwxX2kvMTYwNDc1MjUyOTc3Mzg5OTc4M19oMTIwMDI4AVg0YgczNjB4NjQwahFXRUJQX1NJTVBMRV9RWTI2NQ==",
    "__NStokensig":"3ecb5ea580463c6ddf3446ed930cd7e804d6c86cf8b2e8fe15ad4eb7770ec50d",
    "os":"android",
    "client_key":"3c2cd3f3",
    "token":"7656d12e70c94d8f8cd9636934e5e7fc-849970873",
    "sig":"31880db7cad1570905fd83064a7475c3",

}
header = {

    "User-Agent": "kwai-android",
    "X-REQUESTID": 130092633,
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "114.118.4.4",

}
postStr = urllib.parse.urlencode(postData).encode("utf8")
req = urllib.request.Request(url=url,headers=header,data=postStr)
context = ssl._create_unverified_context()
response = urllib.request.urlopen(req,context=context)
print(response.read().decode("utf-8"))
