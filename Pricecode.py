from Product import Product
from Shop import Shop

#Shops
s1 = Shop("Aldi",(240,230))
s2 = Shop("Real",(120,330))
s3 = Shop("Netto",(140,280))
s4 = Shop("Edeka",(200,189))

#Produkten
#Aldi
s1.stock.append(Product(product_name="Butter", price=10.0, barCode=305764015599))
s1.stock.append(Product(product_name="Milch", price=0.61, barCode=305764011155))
s1.stock.append(Product("Wasser", 1.5, 3057640181432))
s1.stock.append(Product("Brot", 2.5, 305764018546))
s2.stock.append(Product("Kaffee", 3.5, 305764011475))
s2.stock.append(Product("Tee", 1.2, 3057640188965))
s2.stock.append(Product("Ice Cream", 0.8, 3057640187452))
s2.stock.append(Product("Schokoladenpudding", 2.5, 3057640184725))
s2.stock.append(Product("Käse", 1.6, 3057640181423))
s2.stock.append(Product("Knoppers", 2.3, 3057640184132))

#Real
s2.stock.append(Product("Butter", 9.8, 305764018475))
s2.stock.append(Product("Milch", 0.65, 305764017465))
s2.stock.append(Product("Wasser", 0.85, 3057640181559))
s2.stock.append(Product("Brot", 1.3, 3057640181478))
s2.stock.append(Product("Kaffee", 4.0, 305764011478))
s2.stock.append(Product("Tee", 3.2, 3057640182563))
s2.stock.append(Product("Ice Cream", 1.5, 3057640181326))
s2.stock.append(Product("Schokoladenpudding", 0.85, 3057640181965))
s2.stock.append(Product("Käse", 2.6, 3057640184729))
s2.stock.append(Product("Knoppers", 2.0, 3057640181032))

#Netto
s3.stock.append(Product("Butter", 9.5, 305764016644))
s3.stock.append(Product("Milch", 0.62, 305764011126))
s3.stock.append(Product("Wasser", 0.50, 3057640181473))
s3.stock.append(Product("Brot", 0.15, 3057640181796))
s3.stock.append(Product("Kaffee", 1.5, 3057640183216))
s3.stock.append(Product("Tee", 1.6, 3057640181726))
s3.stock.append(Product("Ice Cream", 1.4, 3057640181563))
s3.stock.append(Product("Schokoladenpudding", 0.6, 3057640184756))
s3.stock.append(Product("Käse", 2.6, 3057640184756))
s3.stock.append(Product("Knoppers", 1.8, 3057640181436))

#Edeka
s4.stock.append(Product("Butter", 9.4, 305764019988))
s4.stock.append(Product("Milch", 0.72, 305764011477))
s4.stock.append(Product("Wasser",2.0, 3057640184999))
s4.stock.append(Product("Brot",2.3, 3057640181144))
s4.stock.append(Product("Kaffee", 4.8, 3057640182263))
s4.stock.append(Product("Tee", 3.6, 3057640181785))
s4.stock.append(Product("Ice Cream", 3.3, 3057640181936))
s4.stock.append(Product("Schokoladenpudding", 3.1, 3057640181578))
s4.stock.append(Product("Käse", 4.2, 3057640181023))
s4.stock.append(Product("Knoppers", 2.5, 305764014726))


all_shops =[s1,s2,s3,s4]
