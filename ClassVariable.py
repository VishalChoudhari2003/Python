#class variable
#circle class
#area,circumference

class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        

    def circumference(self):
        return 2*Circle.pi*self.radius
    
c1=Circle(5)
print(c1.circumference())