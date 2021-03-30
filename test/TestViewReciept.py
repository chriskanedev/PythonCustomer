import unittest

from src.Engine.view_receipt import create_receipt


class MyTestCase(unittest.TestCase):
    def testCreateReceipt1(self):

        menu = {"tea": 2.40, "coffee": 2.50}
        quantity = {"tea": 2, "coffee": 1}
        result = create_receipt(menu, quantity)
        self.assertEqual(result, ['Order Number:TEST00', 2, 'tea', '£2.4', 1, 'coffee', '£2.5', 7.3])

    def testCreateReceipt2(self):
        menu = {"tea": 2.40, "coffee": 2.50, "green tea": 2.60}
        quantity = {"tea": 2, "coffee": 1, "green tea": 0}
        result = create_receipt(menu, quantity)
        self.assertEqual(result, ['Order Number:TEST00', 2, 'tea', '£2.4', 1, 'coffee', '£2.5', 7.3])

    def testCreateReceipt3(self):
        menu = {"tea": 2.40, "coffee": 2.50, "Free Gift": 0.00}
        quantity = {"tea": 2, "coffee": 1, "Free Gift": 2}
        result = create_receipt(menu, quantity)
        self.assertEqual(result, ['Order Number:TEST00', 2, 'tea', '£2.4', 1, 'coffee', '£2.5', 2,'Free Gift', '£0.0', 7.3])

if __name__ == '__main__':
    unittest.main()
