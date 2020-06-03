import requests

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%BC%A0%E4%B8%89%E4%B8%B0&oq=PHP%2520Fatal%2520error%253A%2520Default%2520value%2520for%2520parameters%2520with%2520a%2520class%2520type%2520hint%2520can%2520onl&rsv_pq=95518e5a0001b7c1&rsv_t=7f94ghYG9pLElGe7%2BknEAJXsIWm5psyzE81TjTaMvQL0JFLHiq5od0DVu%2B0&rqlang=cn&rsv_enter=0&inputT=11327&rsv_sug3=85&rsv_sug1=55&rsv_sug7=100&rsv_sug2=0&rsv_sug4=12241'

data = requests.get(url)
print(data.text)