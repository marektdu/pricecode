class Shop():

    def __init__(self, shop_name, location=None):
        self.shop_name = shop_name
        self.location = location
        self.stock = []

s1 = Shop(shop_name= "Milk Shop")
print('Shop info',s1.shop_name,s1.location,len(s1.stock))