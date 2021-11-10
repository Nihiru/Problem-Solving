class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.position = 0
        self.won = False

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos

    def set_won(self, won):
        self.won = won

    def get_name(self):
        return self.name
