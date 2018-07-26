import unittest
import Comparator
from Product import Product
from Shop import Shop

class TestStockMethods(unittest.TestCase):

    def test_water_in_stock(self):

        s1 = Shop(shop_name="Milk Shop")

        p1 = Product(product_name="Butter", price=10.0, barCode=None)
        p2 = Product(product_name="Milch", price=1.35, barCode=None)
        p3 = Product("Wasser", 1.5, 3057640182693)

        s1.stock.append(p1)
        s1.stock.append(p2)
        s1.stock.append(p3)

        self.assertEqual(s1.in_stock(12345678),None)
        self.assertEqual((s1.in_stock(3057640182693)).product_name, 'Wasser')


class Test_comporator(unittest.TestCase):

    def test_comporator(self):
        cc = Comparator.Comparator()

        self.assertEqual(cc.add(1,1),2)




if __name__ == '__main__':
    unittest.main()
