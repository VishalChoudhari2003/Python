#Encapsulation
#Abstraction
#Evrything is public in python within in class


class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model=model_name
        self.__price=price

    def make_call(self,phone_no):
        print(f"Calling {phone_no}...")

    def full_name(self):
        return f"{self.brand} {self.model}"
    

p1=Phone('Iphone','16 PRO',150000)
print(p1.brand,p1.model)
#__name private method ke liye syntax
#__name__  dunder/magic method

#Name Mangling 
#print(p1.price)

#__name
print(p1._Phone__price)
