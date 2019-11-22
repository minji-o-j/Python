x1=int(input("큰 원의 중심좌표 x1: "))
y1=int(input("큰 원의 중심좌표 y1: "))
r1=int(input("큰 원의 반지름 r1: "))
x2=int(input("작은 원의 중심좌표 x2: "))
y2=int(input("작은 원의 중심좌표 y2: "))
r2=int(input("작은 원의 반지름 r2: "))
dis=((x1-x2)**2+(y1-y2)**2)**0.5

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(x1,y1-r1)
t.down()
t.circle(r1)
t.up()
t.goto(x2,y2-r2)
t.down()
t.circle(r2)

if(dis<=r1-r2):
    t.write("    작은 원은 큰 원의 내부에 있습니다.")
elif(dis<r1+r2):
    t.write("    작은 원은 큰 원과 걸쳐있습니다.")
else:
    t.write("    작은 원은 큰 원의 외부에 있습니다.")
