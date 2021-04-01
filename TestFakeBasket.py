import unittest

from src.Engine.Basket import *


class basketTest(unittest.TestCase):

    def testBasketFake1(self):
        testMenu = {"Coffee": 2.50, "Tea": 2.40, "Donut": 2.70, "Cake": 3.00}
        testAmountOfItem = {"Coffee": 0, "Tea": 1, "Donut": 2, "Cake": 3}
        testResult = basket(testMenu, testAmountOfItem)
        print(testResult)
        self.assertEqual(testResult,[{"Coffee": 2.50, "Tea": 2.40, "Donut": 2.70, "Cake": 3.00}, {"Coffee": 0, "Tea": 1, "Donut": 2, "Cake": 3} ])

    def testBasketFake2(self):
        testMenu = {"Coffee": 2.50, "Tea": 2.40, "Donut": 2.70, "Cake": 3.00}
        testAmountOfItem = {"Coffee": 5, "Tea": 4, "Donut": 3, "Cake": 6}
        testResult = basket(testMenu, testAmountOfItem)
        print(testResult)
        self.assertEqual(testResult,[{"Coffee": 2.50, "Tea": 2.40, "Donut": 2.70, "Cake": 3.00}, {"Coffee": 5, "Tea": 4, "Donut": 3, "Cake": 6} ])

if __name__ == '__main__':
    unittest.main()

