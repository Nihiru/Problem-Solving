import random


class Dice:

    def __init__(self, minimum, maximum, curr_value) -> None:
        self.min_value = minimum
        self.max_value = maximum
        self.current_value = curr_value

    def roll(self):
        return random.randint(self.min_value, self.max_value + 1)
