import math


class Dice:

    def __init__(self, min, max, curr_value) -> None:
        self.min_value = min
        self.max_value = max
        self.current_value = curr_value
