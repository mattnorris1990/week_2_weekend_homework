import unittest

from src.room import *
from src.guest import *
from src.song import *
from src.drink import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 3, 10)
        self.room_2 = Room("Room 2", 5, 15)
        self.room_2 = Room("Room 3", 7, 20)

        self.song_1 = Song("Take on Me", "a-ha")
        self.song_2 = Song("Wuthering Heights", "Kate Bush")
        self.song_3 = Song("Bodies", "Drowning Pool")
        self.song_4 = Song("Since U Been Gone", "Kelly Clarkson")

        self.guest_1 = Guest("Stuart", 10, "Take on Me")
        self.guest_2 = Guest("John", 15, "Wuthering Heights")
        self.guest_3 = Guest("Keith", 20, "Bodies")
        self.guest_4 = Guest("Kris", 25, "Since U Been Gone")
        self.guest_5 = Guest("Matt", 4, "Kiss From a Rose")

        self.drink_1 = Drink("Screwdriver", 3, 10)
        self.drink_2 = Drink("Sex on the Beach", 4, 2)
        self.drink_3 = Drink("White Russian", 5, 5)

    def test_room_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(3, self.room_1.capacity)

    def test_add_to_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.assertEqual(["Stuart"], self.room_1.guest_list)

    def test_add_multiple_to_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.add_guest_to_guest_list(self.guest_3)
        self.assertEqual(["Stuart", "John", "Keith"], self.room_1.guest_list)

    def test_remove_guest_from_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.add_guest_to_guest_list(self.guest_3)
        self.assertEqual(["Stuart", "John", "Keith"], self.room_1.guest_list)
        self.room_1.remove_guest_from_guest_list(self.guest_3)
        self.assertEqual(["Stuart", "John"], self.room_1.guest_list)

    def test_add_song_to_room(self):
        self.room_1.add_song_to_song_list(self.song_1)
        self.assertEqual(["Take on Me"], self.room_1.song_list)

    def test_remove_song_from_song_list(self):
        self.room_1.add_song_to_song_list(self.song_1)
        self.room_1.add_song_to_song_list(self.song_3)
        self.assertEqual(["Take on Me", "Bodies"], self.room_1.song_list)
        self.room_1.remove_song_from_song_list(self.song_1)
        self.assertEqual(["Bodies"], self.room_1.song_list)

    def test_room_capacity_reached(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.add_guest_to_guest_list(self.guest_3)
        self.room_1.add_guest_to_guest_list(self.guest_4)
        self.assertEqual(["Stuart", "John", "Keith"], self.room_1.guest_list)
        self.assertEqual("room full - added to waiting list", self.room_1.add_guest_to_guest_list(self.guest_4))

    def test_check_guest_can_afford(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_5)
        self.assertEqual(["Stuart"], self.room_1.guest_list)

    def test_check_guest_can_afford_return(self):
        self.assertEqual("cannot afford room", self.room_1.add_guest_to_guest_list(self.guest_5))

    def test_check_guest_has_paid(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.assertEqual(0, self.guest_1.wallet)

    def test_check_till_amount(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.assertEqual(10, self.room_1.till)

    def test_check_till_amount_multiple(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.assertEqual(20, self.room_1.till)

    def test_add_drink_to_bar(self):
        self.room_1.add_drink_to_bar(self.drink_1)
        self.assertEqual(["Screwdriver"], self.room_1.bar)

    def test_sell_drink(self):
        self.room_1.add_drink_to_bar(self.drink_1)
        self.room_1.add_drink_to_bar(self.drink_2)
        self.room_1.sell_drink(self.drink_1, self.guest_1)
        self.assertEqual(["Sex on the Beach"], self.room_1.bar)
        self.assertEqual(9, self.drink_1.stock)
        self.assertEqual(7, self.guest_1.wallet)
        self.assertEqual(3, self.room_1.till)

    def test_sell_drink_cant_afford(self):
        self.room_1.add_drink_to_bar(self.drink_3)
        self.assertEqual("cannot afford drink", self.room_1.sell_drink(self.drink_3, self.guest_5))

    def test_sell_drink_not_available(self):
        self.room_1.add_drink_to_bar(self.drink_3)
        self.assertEqual("drink not available", self.room_1.sell_drink(self.drink_1, self.guest_1))

    def test_add_to_waiting_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.add_guest_to_guest_list(self.guest_3)
        self.room_1.add_guest_to_guest_list(self.guest_4)
        self.assertEqual(["Kris"], self.room_1.waiting_list)

    def test_clear_room_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.room_1.add_guest_to_guest_list(self.guest_2)
        self.room_1.add_guest_to_guest_list(self.guest_3)
        self.room_1.add_guest_to_guest_list(self.guest_4)
        self.assertEqual(None, self.room_1.clear_guest_list())
