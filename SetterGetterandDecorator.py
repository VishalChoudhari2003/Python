

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
print(p1.full_name())