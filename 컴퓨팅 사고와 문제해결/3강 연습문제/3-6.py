a=int(input("x1: "))
b=int(input("y1: "))
c=int(input("x2: "))
d=int(input("y2: "))

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(a,b)
t.down()
t.goto(c,d)
t.write("직선의 길이 = "+str(((a-c)**2+(b-d)**2)**0.5))
