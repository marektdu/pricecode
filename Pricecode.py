from Product import Product
from Shop import Shop


def define_shops():
    """Shops"""

    s1 = Shop("Aldi",(240,230))
    s2 = Shop("Real",(120,330))
    s3 = Shop("Netto",(140,280))
    s4 = Shop("Edeka",(200,189))

    return [s1,s2,s3,s4]

def fill_shop_stocks(shops):
    """fill wıth products"""


    #Aldi
    shops[0].stock.append(Product(product_name="Butter", price=10.0, barCode=305764015599))
    shops[0].stock.append(Product(product_name="Milch", price=0.61, barCode=305764011155))
    shops[0].stock.append(Product("Wasser", 1.5, 3057640181432))
    shops[0].stock.append(Product("Brot", 2.5, 305764018546))
    shops[0].stock.append(Product("Kaffee", 3.5, 305764011475))
    shops[0].stock.append(Product("Tee", 1.2, 3057640188965))
    shops[0].stock.append(Product("Ice Cream", 0.8, 3057640187452))
    shops[0].stock.append(Product("Schokoladenpudding", 2.5, 3057640184725))
    shops[0].stock.append(Product("Käse", 1.6, 3057640181423))
    shops[0].stock.append(Product("Knoppers", 2.3, 3057640184132))

    #Real
    shops[1].stock.append(Product("Butter", 9.8, 305764018475))
    shops[1].stock.append(Product("Milch", 0.65, 305764017465))
    shops[1].stock.append(Product("Wasser", 0.85, 3057640181559))
    shops[1].stock.append(Product("Brot", 1.3, 3057640181478))
    shops[1].stock.append(Product("Kaffee", 4.0, 305764011478))
    shops[1].stock.append(Product("Tee", 3.2, 3057640182563))
    shops[1].stock.append(Product("Ice Cream", 1.5, 3057640181326))
    shops[1].stock.append(Product("Schokoladenpudding", 0.85, 3057640181965))
    shops[1].stock.append(Product("Käse", 2.6, 3057640184729))
    shops[1].stock.append(Product("Knoppers", 2.0, 3057640181032))

    #Netto
    shops[2].stock.append(Product("Butter", 9.5, 305764016644))
    shops[2].stock.append(Product("Milch", 0.62, 305764011126))
    shops[2].stock.append(Product("Wasser", 0.50, 3057640181473))
    shops[2].stock.append(Product("Brot", 0.15, 3057640181796))
    shops[2].stock.append(Product("Kaffee", 1.5, 3057640183216))
    shops[2].stock.append(Product("Tee", 1.6, 3057640181726))
    shops[2].stock.append(Product("Ice Cream", 1.4, 3057640181563))
    shops[2].stock.append(Product("Schokoladenpudding", 0.6, 3057640184756))
    shops[2].stock.append(Product("Käse", 2.6, 3057640184756))
    shops[2].stock.append(Product("Knoppers", 1.8, 3057640181436))

    #Edeka
    shops[3].stock.append(Product("Butter", 9.4, 305764019988))
    shops[3].stock.append(Product("Milch", 0.72, 305764011477))
    shops[3].stock.append(Product("Wasser",2.0, 3057640184999))
    shops[3].stock.append(Product("Brot",2.3, 3057640181144))
    shops[3].stock.append(Product("Kaffee", 4.8, 3057640182263))
    shops[3].stock.append(Product("Tee", 3.6, 3057640181785))
    shops[3].stock.append(Product("Ice Cream", 3.3, 3057640181936))
    shops[3].stock.append(Product("Schokoladenpudding", 3.1, 3057640181578))
    shops[3].stock.append(Product("Käse", 4.2, 3057640181023))
    shops[3].stock.append(Product("Knoppers", 2.5, 305764014726))


def main():

    all_shops = define_shops()
    fill_shop_stocks(all_shops)


if __name__ == """__main__""":
    main()

