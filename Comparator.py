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

    @staticmethod
    def distance(point_1,point_2):
        distance = (( point_1[0]- point_2[0]) ** 2 + (point_1[1]- point_2[1]) ** 2) ** .5
        return distance

    def shops_in_range(self,desired_range, your_location,shops):

        shops_in_range = []

        for shop in shops:

            distance = self.distance(your_location, shop.location)

            if distance < desired_range:

                shops_in_range.append(shop)

        return shops_in_range


    def get_priceless_prduct(self, product_list):

        #product_shop_list [ (product_y, shop_z),(product_x, shop_j), ...]

        product_shop_list = []
        product_found = product_list[0][0]
        shop_found    = product_list[0][1]
        
        for product, shop in product_list:
            if product_found.price > product.price:
                product_found = product
                shop_found    = shop
        return (product_found, shop_found )


    def add(self, val1, val2):


        return val1 + val2