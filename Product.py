class Product():

    def  __init__(self,product_name,price,barCode):
        self.product_name = product_name
        self.price = price
        self.barCode = barCode


p1 = Product (product_name="Butter",price=10.0,barCode=None)
p2 = Product (product_name="Milch",price=1.35,barCode=None)
print('my prıce is', p1.price)
print('my prıce is', p2.price)