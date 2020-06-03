
a = [
    {
        "id":1,
        "name":"水果",
        "parent":0
    },
    {
        "id":2,
        "name":"电子产品",
        "parent":0
    },
    {
        "id":3,
        "name":"苹果",
        "parent":1
    },
    {
        "id":4,
        "name":"黑苹果",
        "parent":3
    },
    {
        "id":5,
        "name":"小黑苹果",
        "parent":4
    },
    {
        "id":6,
        "name":"小小黑苹果",
        "parent":5
    },
    {
        "id":7,
        "name":"小小小黑苹果",
        "parent":6
    }
]

def getNav(a):
    nav = []
    for item in a.items(:
        if item['parent']==0:
            nav.append(item)
        else:
            for i in nav:
                if i["id"]==item['parent']:
                    i["chirldren"] = item
                else:
                    getNav(a)



print(getNav(a))