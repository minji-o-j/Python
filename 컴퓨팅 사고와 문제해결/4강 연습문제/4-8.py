
p=[]
a=int(input("x1: "))
p.append(a)
a=int(input("y1: "))
p.append(a)
a=int(input("x2: "))
p.append(a)
a=int(input("y2: "))
p.append(a)
a=int(input("x3: "))
p.append(a)
a=int(input("y3: "))
p.append(a)

import turtle
t=turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(p[0],p[1])
t.down()
t.goto(p[2],p[3])
t.goto(p[4],p[5])
