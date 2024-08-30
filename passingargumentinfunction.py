'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument
4. keyword variable length argument
'''

def person(name,age):
    print("name=",name)
    age=age+10
    print("age=",age)

#1. postional arguments
person('abcd',223)
#person(66,'asda')

#2. keyword argument
person(name="ram",age=66)
person(age=888,name='ref')

def ad(x,y,z):
    s=x+y+z
    print(s)

ad(55,66,56)

#3  variable length argument
def add(x,*y):
    # print(x)
    # print(y)
    sum=x
    for i in y:
        #print(i)
        sum=sum+i
    print(sum)
add(55,666,345)


def add1(*y):
    # print(x)
    # print(y)
    sum=0
    for i in y:
        #print(i)
        sum=sum+i
    print(sum)
add1(55,666,345)

#4. keyword variable length argument
def persondata(**data):
    print(data)
    for i,j in data.items():
        print(i,j)

#persondata('rohan',55,'545435435','gkp',666)
persondata(name="ashwani",age=55,city='gkp')