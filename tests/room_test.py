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
        self.assertEqual("room full", self.room_1.add_guest_to_guest_list(self.guest_4))