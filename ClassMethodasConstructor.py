#class methods

#instance methods
class Person:
    def __init__(self,first_name,last_name,age):
        self.first=first_name
        self.last=last_name
        self.age=age

    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)

    #Class Method
    @classmethod
    def count_instances(cls):
        return f"You have created{cls.count_instances}instances of person Class"

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def is_above_18(self):
        return self.age>18


p1=Person('Vishal','Choudhari',22)
#/print(p1.full_name())
#print(p1.is_above_18())
#print(Person.count_instances())  #for class method
##print(Person.full_name(p1))##
p2=Person.from_string("Vishal,Choudhari,22")
print(p2.first)
