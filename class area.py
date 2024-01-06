import math
class Cricle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
r=int(input("Enter radius of cricle:"))       
r1=Cricle(r)
print("Area of Cricle:",r1.area())
print("Perimeter Of Cricle:",r1.perimeter())


