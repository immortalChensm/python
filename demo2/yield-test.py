
def run():
    for i in range(0,10):
        yield i


gen = run()
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())

