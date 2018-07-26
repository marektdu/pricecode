from Product import Product
from Shop import Shop


#Produkten
#Aldi
p1.1 = Product (product_name="Butter", price=10.0, barCode=None)
p2.1 = Product (product_name="Milch", price=0.61, barCode=None)
p3.1 = Product ("Wasser", 1.5, 3057640182693)
p4.1 = Product ("Brot", 2.5, 3057640182693)
p5.1 = Product ("Kaffee")
p6.1 = Product ("Tee")
p7.1 = Product ("Ice Cream")
p8.1 = Product ("Kaffee")
p9.1 = Product ("Kaffee")

#Real
p1.2 = Product ("Butter", 9.8, None)
p2.2 = Product ("Milch", 0.65, None)
p3.2 = Product ("Wasser", 1.5, 3057640182693)
p4.2 = Product ("Brot", 2.5, 3057640182693)
p5.1 = Product ("Kaffee")
p6.1 = Product ("Tee")
p7.1 = Product ("Ice Cream")
p8.1 = Product ("Kaffee")
p9.1 = Product ("Kaffee")

#Netto
p1.3 = Product ("Butter", 9.5, None)
p2.3 = Product ("Milch", 0.62, None)
p3.3 = Product ("Wasser",1.5, 3057640182693)
p4.3 = Product ("Brot",2.5, 3057640182693)
p5.1 = Product ("Kaffee")
p6.1 = Product ("Tee")
p7.1 = Product ("Ice Cream")
p8.1 = Product ("Kaffee")
p9.1 = Product ("Kaffee")

#Edeka
p1.4 = Product ("Butter", 9.4, None)
p2.4 = Product ("Milch", 0.72, None)
p3.4 = Product ("Wasser",1.5, 3057640182693)
p4.4 = Product ("Brot",2.5, 3057640182693)
p5.1 = Product ("Kaffee")
p6.1 = Product ("Tee")
p7.1 = Product ("Ice Cream")
p8.1 = Product ("Kaffee")
p9.1 = Product ("Kaffee")

#Stock Append
s1.stock.append(p1.1)
s1.stock.append(p2.1)
s1.stock.append(p3.1)
s2.stock.append(p4.2)

#Shops
s1 = Shop("Aldi",)
s2 = Shop("Real")
s3 = Shop("Netto")
s4 = Shop("Edeka")

all_shops =[s1,s2,s3,s4]

