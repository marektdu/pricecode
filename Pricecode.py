from Product import Product
from Shop import Shop

p1 = Product (product_name="Butter",price=10.0,barCode=None)
p2 = Product (product_name="Milch",price=1.35,barCode=None)
print('my prıce is', p1.price)
print('my prıce is', p2.price)

s1 = Shop(shop_name= "Milk Shop")
print('Shop infoold',s1.shop_name,s1.location,len(s1.stock))
s1.stock.append(p1)
s1.stock.append(p2)
print('Shop infonew',s1.shop_name,s1.location,len(s1.stock))