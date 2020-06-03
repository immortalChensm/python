import os
BASE_DIR = os.path.dirname(__file__)
options = {
    "port":9000
}

settings = {
    "debug":False,
    "static_path":os.path.join(BASE_DIR,"static"),
    "template_path":os.path.join(BASE_DIR,"templates"),
    #"autoescape":None,#关闭所有模板文件的自动转义
    "cookie_secret":"zeDXPHQ3QO2f7thhNE7sVTjuHUT9Pkg+lZ6tE5l/Ez8=",
    #"xsrf_cookies":True,
    "login_url":"/login"
}
