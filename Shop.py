class Shop():

    def __init__(self, shop_name, location=None):
        self.shop_name = shop_name
        self.location = location
        self.stock = []

    def in_stock(self, barcode):
        for pp in self.stock:
          #  print (pp.product_name)
            if barcode == pp.barCode:
                return pp

        return None