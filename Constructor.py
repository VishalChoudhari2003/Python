#contructor in python
class Person:
    def __init__(self,name,occupation):     #contructor method
        self.name=name
        self.occ=occupation

    def info(self):
        print(f"{self.name} is a {self.occ}")


a=Person('Vishal','Student')
b=Person('Vishal','Student')
a.info()
b.info()