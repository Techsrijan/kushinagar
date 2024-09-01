'''
penup=pu
pendown=pd
forward=fd

'''

from turtle import *
t=Turtle()
t.shape('turtle')
t.hideturtle()
t.speed(1)
t.pensize(20)
# t.pencolor('red')
# t.fillcolor('green')
t.color('red','green')
t.begin_fill()
t.fd(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()
t.penup()
t.forward(100)
t.pendown()
t.forward(100)
for i in range(3):
    t.left(90)
    t.forward(100)

t.backward(200)
done()