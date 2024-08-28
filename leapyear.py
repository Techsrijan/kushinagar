year=int(input("enter any year"))
if year%100==0:
    if year%400==0:
        print("leap year=", year)
    else:
        print("not leap year=", year)

elif year%4==0:
    print("leap year=",year)
else:
    print("not leap=",year)