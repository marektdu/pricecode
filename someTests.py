import unittest
import Comparator
from Product import Product
from Shop import Shop

class TestStockMethods(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(Comparator.Comparator.distance((1,1),(1,1)),0)
        self.assertAlmostEqual(Comparator.Comparator.distance((0,0), (1, 1)), 1.4142,4)

    def define_test_data(self):
        s1 = Shop("Aldi", (10,10))
        s2 = Shop("Real", (200,200))

        p1 = Product(product_name="Butter", price=10.0, barCode=None)
        p2 = Product(product_name="Milch", price=0.61, barCode=None)
        p3 = Product("Wasser", 1.5, 3057640182693)
        p4 = Product("Brot", 2.5, 3057640182693)

        s1.stock.append(p1)
        s1.stock.append(p2)
        s1.stock.append(p3)
        s1.stock.append(p4)

        p5 = Product("Butter", 9.8, None)
        p6 = Product("Milch", 0.65, None)
        p7 = Product("Wasser", 1.5, 3057640182693)
        p8 = Product("Brot", 2.5, 3057640182693)

        s2.stock.append(p5)
        s2.stock.append(p6)
        s2.stock.append(p7)
        s2.stock.append(p8)

        self.shops = [s1, s2]

    def test_water_in_stock(self):

        self.define_test_data()

        cc = Comparator.Comparator()
        self.assertEqual(cc.in_stock(12345678,self.shops),[])
        self.assertEqual(cc.in_stock(3057640182693,self.shops)[0][0].product_name, 'Wasser')

    def test_shops_in_range(self):
        self.define_test_data()

        cc = Comparator.Comparator()

        shop_list = cc.shops_in_range(desired_range=100, your_location=(0,0),shops=self.shops)
        self.assertEqual(shop_list[0].shop_name, "Aldi")

class Test_comporator(unittest.TestCase):

    def test_comporator(self):
        cc = Comparator.Comparator()

        self.assertEqual(cc.add(1,1),2)




if __name__ == '__main__':
    unittest.main()
