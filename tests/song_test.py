import unittest

from src.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Take on Me", "a-ha")
        self.song_2 = Song("Wuthering Heights", "Kate Bush")
        self.song_3 = Song("Bodies", "Drowning Pool")
        self.song_4 = Song("Since U Been Gone", "Kelly Clarkson")

    def test_song_name(self):
        self.assertEqual("Bodies", self.song_3.name)

    def test_song_artist(self):
        self.assertEqual("Drowning Pool", self.song_3.artist)
