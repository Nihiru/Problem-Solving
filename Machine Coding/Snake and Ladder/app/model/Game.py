import random
from collections import deque

from Ladder import Ladder
from Dice import Dice
from Board import Board
from Player import Player
from Snake import Snake


class Game:
    def __init__(self,
                 number_of_ladders,
                 number_of_snakes,
                 board_size
                 ) -> None:
        self.number_of_ladders = number_of_ladders
        self.number_of_snakes = number_of_snakes
        self.board = Board(board_size)
        self.players = deque([Player])
        self.snakes = list(Snake)
        self.ladders = list(Ladder)
        self.dice = Dice(1, 6, 2)
        self.init_board()

    def init_board(self):
        snake_ladder_set = set()
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
                """
                1) making sure the `snake` entity brings down a user from its head position to its tail position
                2) tail should be greater than head position
                """
                if snake_tail >= snake_head:
                    continue

                head_tail_pair = str(snake_head) + str(snake_tail)
                if head_tail_pair in snake_ladder_set:
                    new_snake = Snake(snake_head, snake_tail)
                    self.snakes.append(new_snake)
                    snake_ladder_set.add(head_tail_pair)
                    break

        for i in range(len(self.ladders)):
            while True:
                ladder_start = random.randint(
                    self.board.get_start(),
                    self.board.get_end()
                )
                ladder_end = random.randint(
                    self.board.get_start(),
                    self.board.get_end()
                )

                if ladder_end <= ladder_start:
                    continue

                start_end_pair = str(ladder_start) + str(ladder_end)
                if start_end_pair in snake_ladder_set:
                    new_ladder = Ladder(ladder_start, ladder_end)
                    self.ladders.append(new_ladder)
                    snake_ladder_set.add(start_end_pair)
                    break

    def add_player(self, player_obj: Player):
        self.players.append(player_obj)

    def play_game(self):
        while True:
            player = self.players.popleft()
            val = self.dice.roll()
            new_position = player.get_position() + val
            if new_position > self.board.get_end():
                player.set_position(player.get_position())
                self.players.append(player)
            else:
                player.set_position(
                    self.check_position_circumstances(new_position)
                )
                if player.get_position() == self.board.get_end():
                    player.set_won = True
                    print(" Player " + player.get_name() + "Won.")
                else:
                    print(" Setting " + player.get_name() +
                          " 's new position to " + player.get_position())
                    self.players.append(player)
            if len(self.players) < 2:
                break

    def check_position_circumstances(self, new_position):
        for snake in self.snakes:
            if snake.get_head() == new_position:
                print("Snake Bit...")
                return snake.get_tail()

        for ladder in self.ladders:
            if ladder.get_end() == new_position:
                print("Climbed ladder...")
                return ladder.get_start()

        return new_position
