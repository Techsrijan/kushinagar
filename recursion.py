'''
when a function calls itself it is called recursion
'''
import sys
sys.setrecursionlimit(sys.getrecursionlimit()+4000)
print(sys.getrecursionlimit())

i=1
def greet():
    global i
    print("good morning=",i)
    i=i+1
    greet() #call

greet()
