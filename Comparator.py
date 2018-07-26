from Shop import Shop

class Comparator ():

    def __init__(self):
        self.all_shops = []


    def in_stock(self, barcode):

        s1 = Shop("Aldi" )
        s2 = Shop("Real")

        all_shops_in_range = [s1 , s2]

        products_found = []

        for shop in all_shops_in_range:
            for product in shop.stock:
            #  print (pp.product_name)
                if barcode == product.barCode:
                    products_found.append((product,shop))

        return products_found



    def add(self, val1, val2):

        return val1 + val2