n=int(input("enter any number"))
sum=0
mul=1

while n>0:
    a=n%10
    sum=sum+a
    mul=mul*a
    n=n//10
print(sum)
print(mul)
if sum==mul:
    print("magic no")
else:
    print("not magic no")
