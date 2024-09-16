f=open("ram.txt","r")
print(f)
#print(f.read())
for data in f:
    print(data,end="")
f.close()

g=open("ram.txt","a")
g.write("fjhfgjfgj")
g.close()

p=open("ram.txt","r")
q=open("shyam.txt","w")

for data in p:
    q.write(data)
p.close()
q.close()

a,b=5,6
sum=a+b

f=open("ram.txt","a")
f.write(str(sum))