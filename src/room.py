class Room:
    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.guest_list = []
        self.song_list = []