from app.model.Game import Game
from app.model.Player import Player


def main_app():
    print("Game Begins!!!")
    board_size = input("Enter the board size")
    number_of_players = input("Enter total number of players")
    number_of_snakes = input("Enter total number of snakes")
    number_of_ladders = input("Enter total number of ladders")

    g = Game(number_of_ladders, number_of_snakes, board_size)

    for player in range(number_of_players):
        player_name = input("Enter player name : ")
        player_obj = Player(player_name)
        g.add_player(player_obj)

    g.play_game()


if __name__ == '__main__':
    main_app()
