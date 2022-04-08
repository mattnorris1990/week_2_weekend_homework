import unittest

from src.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Stuart")
        self.guest_2 = Guest("John")
        self.guest_3 = Guest("Keith")
        self.guest_4 = Guest("Kris")

    def test_guest_name(self):
        self.assertEqual("Stuart", self.guest_1.name)