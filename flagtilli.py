from turtle import *
t=Turtle()
t.circle(100)
t.pu()
t.left(90)
t.fd(100)
t.pd()
t.fd(100)
t.backward(100)
for i in range(24):
    t.left(15)
    t.forward(100)
    t.backward(100)
done()