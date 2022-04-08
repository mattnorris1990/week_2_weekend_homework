import unittest

from src.guest import *
from src.room import *
from src.song import *

class TestGuest(unittest.TestCase):
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

    def test_guest_name(self):
        self.assertEqual("Stuart", self.guest_1.name)

    def test_check_song_list_for_favourite_song(self):
        self.room_1.add_song_to_song_list(self.song_1)
        self.assertEqual("THAT'S MY JAM OH YEAHHH", self.guest_1.check_for_favourite_song(self.room_1))
    
    def test_check_song_list_for_favourite_song(self):
        self.room_1.add_song_to_song_list(self.song_2)
        self.assertEqual(None, self.guest_1.check_for_favourite_song(self.room_1))