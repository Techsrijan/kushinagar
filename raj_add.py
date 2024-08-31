def add(x,y):
    c=x+y
    print("sum=",c)

print(__name__)

if __name__=="__main__":
    def msg():
        print("hi")
    msg()
else:
    print("this is not accessible")