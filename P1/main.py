
from game import TicTacToe
from player import RandomGamePlayer

def main() -> None:
    print("hi")

    game = TicTacToe(num_players = 2, size = 3, print_each_move = True)
    player = RandomGamePlayer(print_each_move = True)
    player.play_game(game)

if __name__ == '__main__':
    main()