from Product import Product
from Shop import Shop

p1 = Product (product_name="Butter",price=10.0,barCode=None)
p2 = Product (product_name="Milch",price=1.35,barCode=None)
p3= Product ("Wasser",1.5, 3057640182693)

s1 = Shop(shop_name= "Milk Shop")
s1.stock.append(p1)
s1.stock.append(p2)
s1.stock.append(p3)

s2 = Shop("Spaetie")
p4= Product ("Wasser",2.5, 3057640182693)
s2.stock.append(p4)

s3 = Shop("Buchladen")

all_shops =[s1,s2,s3]

