from functools import reduce
def add(x,y):
    return(x+y)

#print(add(5,6))



'''
Lambda function--to pass function as an argument
a function can take any number of arguments
but a function can have only one expression
'''
f=lambda x,y:x+y
print(f(5,4))


# filter map and reduce
l=[2,55,3,66,33,77,333,88,44]
even_no=list(filter(lambda n:n%2==0,l))
print(even_no)

data=list(map(lambda n:n+10,even_no))
print(data)

result=reduce(lambda a,b:a+b,data)
print(result)