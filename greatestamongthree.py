a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("c is greatest")
elif b>c:
    print("B is greatest")
else:
    print("C is greatest")