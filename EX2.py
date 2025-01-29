class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand=brand_name
        self.model=model_name
        self.price=price

    def apply_discount(self,num):
        #self.price
        off_price=(num/100)*self.price
        return self.price-off_price

l1=Laptop("Dell","G15",60000)
l2=Laptop('Hp','pavilion',55000)

print(l2.apply_discount(5))

print(l1.__dict__)