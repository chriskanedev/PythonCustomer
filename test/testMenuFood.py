import unittest

from unittest.mock import MagicMock
import src.Engine.food_from_menu
from src.Engine import food_from_menu

#to ensure value locking for testing have is_testing return True

class MyTestCase(unittest.TestCase):
    def test_input(self):
        mock_menu = {"tea": 2.40, "coffee": 2.50, "green tea": 2.60}
        src.Engine.food_from_menu.input_menu = MagicMock(return_value=mock_menu)
        result = food_from_menu.orderInput(src.Engine.food_from_menu.input_menu.return_value)
        self.assertEqual(result, [{'tea': 4, 'coffee': 0, 'green tea': 0}])


if __name__ == '__main__':
    unittest.main()
