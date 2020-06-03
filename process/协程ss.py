

def run():
    data = ""
    res = yield data
    print(res)

if __name__=='__main__':

    res = run()
    res.send(None)
    res.send('hi')
