from math import *
#function body
def greet():
    print("good morning")


def msg():
    print("thank you")

#function call
msg()
greet()
msg()


def gumnam():
    pass


def add(a,b):  # here a and b are called formal argument
    c=a+b
    print("sum=",c)

add(5,2)

x=int(input("enter any number"))
y=int(input("enter any number"))

add(x,y)  #here x and y are caled actual argument

print("The square root is=",sqrt(25))


# function return value
def sub(p,q):
    s=p-q
    d=p*q
    return s,d

print(sub(55,5))
op1,op2=sub(232,56)
print(op1,op2)

print(floor(-3.2))
