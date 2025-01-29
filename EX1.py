#Create a laptop class  with attributes like brand name model name ,price
#create two objects/instances of your laptop class


class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand=brand_name
        self.model=model_name
        self.price=price


l1=Laptop("Dell","G15",60000)
l2=Laptop('Hp','pavilion',55000)

print(l1.brand,l1.model,l1.price)
print(l2.brand,l2.model,l2.price)