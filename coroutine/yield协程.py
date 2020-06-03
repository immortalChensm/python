
def run():
    data = ""
    r = yield data
    print(1,r,data)

    r = yield data
    print(2,r,data)

    r = yield data
    print(3,r,data)

m = run()
print(m)
print(next(m))

m.send('a')
m.send('b')
m.send('c')