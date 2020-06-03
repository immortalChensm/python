
'''

for i in range(10):

    print(i)
    if i == 5:
        break
num = 10
while num>=1:
    print(num)
    num-=1
    if num==3:
        break
        num = 1
while num < 5:
    print(num)
    num+=1
    if num == 3:
        break
else:
    print("我做完了")
import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
code = []
for i in range(6):
    code.append(char[random.randrange(0,len(char))])

print("".join(code))

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)


turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

turtle.right(90)
turtle.forward(200)

turtle.forward(100)
turtle.left(45)
turtle.forward(100)
#turtle.speed(10)
turtle.goto(100,-200)

turtle.up()

turtle.goto(300,-100)
turtle.down()
turtle.left(45)
turtle.pensize(10)
turtle.forward(100)
turtle.backward(50)
turtle.left(90)
turtle.forward(100)
'''

import turtle
turtle.pensize(10)
turtle.forward(100)
turtle.backward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.backward(100)
turtle.pencolor("red")
#turtle.reset()
#turtle.clear()

#turtle.circle(50)
#turtle.circle(50,5)
turtle.begin_fill()
turtle.fillcolor("green")
turtle.circle(50,steps=8)
turtle.end_fill()

turtle.forward(100)
turtle.undo()
turtle.hideturtle()
turtle.showturtle()
turtle.done()