import wxpy
import threading
import requests
# print(dir(wxpy))
#
# for item in dir(wxpy):
#     print(item)
#
class Test():
    def __init__(self,result):
        print(result)
def run():
    bot = wxpy.Bot()
    url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx43309b44b1227ffb&redirect_uri=https%3A%2F%2Fmobile5.51ckjr.com%2Fapi%2Fmp%2FauthCallback%3Fpu%3Dhttps%253A%252F%252Fmobile5.51ckjr.com%252Fkpv2p%252Fn9v8%26mpMode%3D3&response_type=code&scope=snsapi_userinfo&state=85ef5bd09d881a77d21a1983a7b92541&connect_redirect=1&pass_ticket=3HZxNmwL6CydVykiCd8%2FkdT5H4slZ%2B%2B99qd6tVNoDqDQu7h1Bo28E%2FL98H8qtA48#time=1535616906000"
    req = wxpy.BaseRequest(bot,url)
    result = req.request('GET',Test)
    print(result)
if __name__=='__main__':

    print("程序启动")
    p = threading.Thread(target=run)
    p.start()
    p.join()


