import unittest

from src.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Screwdriver", 3, 10)
        self.drink_2 = Drink("Sex on the Beach", 4, 2)
        self.drink_3 = Drink("White Russian", 5, 5)

    def test_has_name(self):
        self.assertEqual("Screwdriver", self.drink_1.name)

    def test_has_price(self):
        self.assertEqual(3, self.drink_1.price)

    def test_has_stock(self):
        self.assertEqual(10, self.drink_1.stock)
