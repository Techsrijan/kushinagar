from turtle import *
from time import *
t=Turtle()
t.pencolor('red')
#t.circle(150)
#t.circle(100,steps=10)
#t.undo()
t.reset()
t.pencolor('green')
#t.circle(-100,extent=-180)
#t.write("Mera bharat Mahan",font=("Comic Sans Ms",10,"bold"))
t.reset()
t.shape('turtle')
i=2
for i in range(10):
    t.stamp()
    i=i+100
    t.pu()
    t.fd(i)
    t.pd()
    sleep(1)
done()