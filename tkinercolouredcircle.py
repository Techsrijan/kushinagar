from turtle import *
t=Turtle()
l=['red','yellow','blue','green','orange']


t.pu()
t.fd(200)
t.pd()
t.pensize(10)
for i in range(3):
    t.pencolor(l[i])
    t.circle(50)
    t.pu()
    t.backward(150)
    t.pd()

done()