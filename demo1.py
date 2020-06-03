import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379,encoding='utf8',decode_responses=True)

keys = r.keys("*")

for k in keys:
    print(k,end='\n')