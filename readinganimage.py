f=open("best.gif","rb")
# for data in f:
#     print(data)

g=open("rest.gif","wb")

for data in f:
    g.write(data)