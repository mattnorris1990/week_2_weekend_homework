class Room:
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.guest_list = []
        self.song_list = []

    def add_guest_to_guest_list(self, guest_to_add):
        self.guest_list.append(guest_to_add.name)