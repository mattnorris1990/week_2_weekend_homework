import unittest

from src.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Stuart", 10, "Take on Me")
        self.guest_2 = Guest("John", 15, "Wuthering Heights")
        self.guest_3 = Guest("Keith", 20, "Bodies")
        self.guest_4 = Guest("Kris", 25, "Since U Been Gone")

    def test_guest_name(self):
        self.assertEqual("Stuart", self.guest_1.name)