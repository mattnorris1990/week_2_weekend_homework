import unittest

from src.room import *
from src.guest import *
from src.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 3)
        self.room_2 = Room("Room 2", 5)
        self.room_2 = Room("Room 3", 7)

        self.song_1 = Song("Take on Me", "a-ha")
        self.song_2 = Song("Wuthering Heights", "Kate Bush")
        self.song_3 = Song("Bodies", "Drowning Pool")
        self.song_4 = Song("Since U Been Gone", "Kelly Clarkson")

        self.guest_1 = Guest("Stuart")
        self.guest_2 = Guest("John")
        self.guest_3 = Guest("Keith")
        self.guest_4 = Guest("Kris")

    def test_room_name(self):
        self.assertEqual("Room 1", self.room_1.name)

    def test_room_capacity(self):
        self.assertEqual(3, self.room_1.capacity)

    def test_add_to_guest_list(self):
        self.add_guest_to_guest_list()
        self.assertEqual("Stuart", self.guest_list)