n=11
i=2
while i<=n-1:
    if n%i==0:
        print("not Prime")
        break
    i=i+1
else:
    print("prime no")