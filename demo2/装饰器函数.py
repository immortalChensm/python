

def outer(func):

    def inner(*args,**kwargs):

        print("&%#####################")
        func(*args,**kwargs)
    return inner


@outer
def say(name,age):
    print("my name is %s,i am %d years old"%(name,age))

say("jack",18)