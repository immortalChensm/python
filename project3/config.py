import os
config = {
    "port":1234
}
BASE_DIRS = os.path.join(os.path.dirname(__file__))
dbconfig = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "passwd":"",
    "dbname":"shop"
}
settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "template_path":os.path.join(os.path.dirname(__file__),"templates"),
    "complied_template_cache":False,
    "static_hash_cache":False,
    #此密钥采用base64 uuid模块生成唯一的
    "cookie_secret":'CAVwhF0PQ7KWo7GlpAZglTu4Mt6h4E6lqvmH64mMksE=',
    #cookie跨域请求保护，防止用户跨域伪造请求 一旦开启此参数，任何请求
    #要修改cookie地操作将会阻止【受保护了】如果在请求页面加上{% module xsrf_form_html() %} 将允许此页面提交
    #修改cookies
    "xsrf_cookies":True,
}
