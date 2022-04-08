from src.guest import *

class Room:
    def __init__(self, input_name, input_capacity, input_booking_cost):
        self.name = input_name
        self.capacity = input_capacity
        self.booking_cost = input_booking_cost
        self.guest_list = []
        self.song_list = []

    def guest_payment_for_room(self, guest_to_pay):
        guest_to_pay.wallet -= self.booking_cost

    def add_guest_to_guest_list(self, guest_to_add):
        if guest_to_add.wallet >= self.booking_cost:
            if len(self.guest_list) < self.capacity:
                self.guest_payment_for_room(guest_to_add)
                self.guest_list.append(guest_to_add.name)
            else:
                return "room full"
        else:
            return "cannot afford room"

    def remove_guest_from_guest_list(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove.name)

    def add_song_to_song_list(self, song_to_add):
        self.song_list.append(song_to_add.name)

    def remove_song_from_song_list(self, song_to_remove):
        self.song_list.remove(song_to_remove.name)