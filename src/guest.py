from src.room import *

class Guest:

    def __init__(self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def check_for_favourite_song(self, current_room):
        for song in current_room.song_list:
            if song == self.favourite_song:
                return "THAT'S MY JAM OH YEAHHH"

