class Room:
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.guest_list = []
        self.song_list = []

    def add_guest_to_guest_list(self, guest_to_add):
        self.guest_list.append(guest_to_add.name)

    def remove_guest_from_guest_list(self, guest_to_remove):
        self.guest_list.remove(guest_to_remove.name)

    def add_song_to_song_list(self, song_to_add):
        self.song_list.append(song_to_add.name)

    def remove_song_from_song_list(self, song_to_remove):
        self.song_list.remove(song_to_remove.name)