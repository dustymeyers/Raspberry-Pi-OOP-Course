class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def describe(self):
        print(self.description)

    def get_description(self):
        return self.description

    def get_details(self):
        print('')
        print('The ' + self.get_name())
        print('-------------------')
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is ' + direction)

    def get_name(self):
        return self.name
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link 
        # for testing purposes
        # print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def set_description(self, room_description):
        self.description = room_description

    def set_name(self, room_name):
        self.name = room_name