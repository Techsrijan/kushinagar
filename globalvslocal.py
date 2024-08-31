p=10 #global variable

x=500
def test():
    x=10 #local variable
    global y #to make a local variable to global
    y=20
    print("Local variable=",x)
    s=globals()['x']
    print("Global variable=",s)

test()
print(p)
print(y)