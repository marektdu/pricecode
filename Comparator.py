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

    @staticmethod
    def distance(self,point_1,point_2):
        distance = (( point_1[0]- point_2[0]) ** 2 + (point_1[1]- point_2[1]) ** 2) ** .5
        return distance

    def shops_in_range(self,desired_range, your_location,shops):

        shops_in_range = []

        for shop in shops:

            distance = ((shop.location_x - your_location[0]) ** 2 + (shop.location_y - your_location[1]) ** 2) ** .5

            if distance < desired_range:

                shops_in_range.append(shop)

        return shops_in_range


    def add(self, val1, val2):

        return val1 + val2