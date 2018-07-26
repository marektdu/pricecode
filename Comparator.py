class Comparator ():

    def __init__(self):
        pass

    #implement functios here

    def get_priceless_prduct(self, product_list):

        #product_shop_list [ (product_y, shop_z),(product_x, shop_j), ...]

        product_shop_list = []
        product_found = product_shop_list[0][0]
        shop_found    = product_shop_list[0][1]
        
        for product, shop in product_shop_list:
            if product_found.price > product.price:
                product_found = product
                shop_found    = shop
        return (product_found, shop_found )


    def add(self, val1, val2):


        return val1 + val2