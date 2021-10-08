from collections import deque

from Dice import Dice
from Board import Board
from Player import Player
from Snake import Snake
from Ladder import Ladder
import random


class Game:
    def __init__(self,
                 number_of_ladders,
                 number_of_snakes,
                 board_size
                 ) -> None:
        self.number_of_ladders = number_of_ladders
        self.number_of_snakes = number_of_snakes
        self.board = Board(board_size)
        self.players = deque(Player)
        self.snakes = list(Snake)
        self.ladder = list(Ladder)
        self.dice = Dice(1, 6, 2)
        self.init_board()

    def init_board(self):
        snake_ladder_set = dict()
        for i in range(len(self.snakes)):
            while True:
                snake_head = random.randint(
                    self.board.get_start(),
                    self.board.get_end()
                )
                snake_tail = random.randint(
                    self.board.get_start(),
                    self.board.get_end()
                )
                # making sure the `snake` entity brings down a user from its head position to its tail position
                if snake_tail >= snake_head:
                    continue
