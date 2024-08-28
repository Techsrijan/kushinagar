a,b,c,d,e=50,40,96,77,99

total=a+b+c+d+e
print("total marks=",total)

per=(total*100)/500
print("percentage=",per)
if per<33:
    print("fail")
elif per>=33 and per<45:
    print("third division")
elif per>=45  and per<60:
    print("second division")
elif per>=60:
    print("first division")