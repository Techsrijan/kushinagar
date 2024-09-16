class Room:   #base class parent
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

#derived class ya child class
#code resuability
class GuestRoom(Room):  # guest room inherits the Room
    pass
    # def area(self,l,b):
    #     self.l=l
    #     self.b=b
    #     print("area=",self.l*self.b)
r=Room()
r.area(4,5)



r1=GuestRoom()
r1.area(4,50)