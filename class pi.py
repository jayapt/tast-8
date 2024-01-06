class a1:
    def __init__(self,r):
        self.r=r
    def area(self):
        self.__pi=3.141 
        return self.__pi*self.r*self.r
a=a1(6)
print("area of a circle private variable in class ",a.area())





