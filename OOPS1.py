#OBJECT ORIENTED PROGRAMMING
#CLASS

#self represent object
#init method is constructor in python
class Person:
    def __init__(self,first_name,last_name,age):
        #instance variables
        print("Init method called")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('Vishal','Choudhari',22)
p2=Person('mohit','Choudhari',21)

print(p1.first_name)