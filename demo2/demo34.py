

def sum1(a):

    sum = 0
    for x in range(1,a+1):
        sum+=x
    return sum



def sum2(a):
    if a==1:
        return 1
    else:
        return a+sum2(a-1)

res = sum2(5)
print("res=",res)