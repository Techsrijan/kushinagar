n=int(input("enter how many toffe you want"))
i=1
stock=15
while n>=i:
    if i<=stock:
        print("Please collect Toffe=",i)

    else:
        print("Out Of stock")
        break
    i=i+1
else: # when loop runs properly
    print("thank you please visit again")