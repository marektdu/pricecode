from Product import Product
from Shop import Shop

#Shops
s1 = Shop("Aldi",(240,230))
s2 = Shop("Real",(120,330))
s3 = Shop("Netto",(140,280))
s4 = Shop("Edeka",(200,189))

#Produkten
#Aldi
s1.stock.append(Product(product_name="Butter", price=10.0, barCode=None))
s1.stock.append(Product(product_name="Milch", price=0.61, barCode=None))
s1.stock.append(Product("Wasser", 1.5, 3057640182693))
s1.stock.append(Product("Brot", 2.5, 3057640182693))

#Real
s2.stock.append(Product("Butter", 9.8, None))
s2.stock.append(Product("Milch", 0.65, None))
s2.stock.append(Product("Wasser", 1.5, 3057640182693))
s2.stock.append(Product("Brot", 2.5, 3057640182693))

#Netto
s3.stock.append(Product("Butter", 9.5, None))
s3.stock.append(Product("Milch", 0.62, None))
s3.stock.append(Product("Wasser",1.5, 3057640182693))
s3.stock.append(Product("Brot",2.5, 3057640182693))

#Edeka
s4.stock.append(Product("Butter", 9.4, None))
s4.stock.append(Product("Milch", 0.72, None))
s4.stock.append(Product("Wasser",1.5, 3057640182693))
s4.stock.append(Product("Brot",2.5, 3057640182693))

all_shops =[s1,s2,s3,s4]

