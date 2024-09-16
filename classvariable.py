class Operation:
    f=5 #class variable
    def add(self,a,b):
        self.a=a   # instance variable
        self.b=b
        self.c=self.a+self.b
        print("total=",self.c)


op=Operation()
op.add(9,10)
print(Operation.f)
print(op.f)
#op.f=50
Operation.f=50
print(op.f)
op1=Operation()
print(op1.f)