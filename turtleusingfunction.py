from turtle import *
t=Turtle()
t.shape('turtle')
t.hideturtle()
t.speed(1)
t.pensize(20)
# t.pencolor('red')
# t.fillcolor('green')
t.color('red','green')
def shape():
    t.fd(100)
    t.left(90)

for i in range(4):
    shape()

shape()
shape()
shape()

done()