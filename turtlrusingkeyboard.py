from turtle import *
t=Turtle()
sc=Screen()
sc.setup(width=500,height=600)
sc.title("My Turtle")
sc.listen()
def moveLeft():
    t.left(90)

def moveRight():
    t.right(90)

def moveFd():
    t.fd(100)

def moveBd():
    t.backward(100)

sc.onkey(moveLeft,"Up")
sc.onkey(moveRight,"Down")
sc.onkey(moveFd,'f')
sc.onkey(moveBd,'b')
done()