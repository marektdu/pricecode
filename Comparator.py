from Shop import Shop

class Comparator ():

    def __init__(self):
        self.all_shops = []


    def in_stock(self, barcode, all_shops_in_range=[]):

        products_found = []

        for shop in all_shops_in_range:
            for product in shop.stock:
            #  print (pp.product_name)
                if barcode == product.barCode:
                    products_found.append((product,shop))

        return products_found



    def add(self, val1, val2):

        return val1 + val2