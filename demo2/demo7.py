
'''
#1553
a = num % 10
b = num //10 % 10
c = num //100 % 10
d = num //1000

print(a,b,c,d)
print(d*1000+c*100+b*10+a*1)

'''

while True:
    num = int(input("entry num:"))

    a = num % 10
    b = num //10 % 10
    c = num // 100

    max = 0
    if a > b:
        max = a
    elif b>c:
        max = b
    elif c>a:
        max = c

    print(max)