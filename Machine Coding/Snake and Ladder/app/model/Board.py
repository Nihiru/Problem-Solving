""" 
A Board is an entity(object) of the Game
"""


class Board:

    def __init__(self, size) -> None:
        self.size = size
        self.start = 1
        self.end = self.start + size - 1

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
