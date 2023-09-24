
from player.player import play_game
from game.tictactoe import TicTacToe
from game.count import Count
from picker.random import RandomMovePicker
from picker.minimax import MinimaxMovePicker

def main() -> None:
    play_game(Count(), RandomMovePicker())
    play_game(Count(goal = 3), MinimaxMovePicker(max_depth = 5))
    # play_game(TicTacToe(), RandomMovePicker())
    # play_game(TicTacToe(), MinimaxMovePicker())

if __name__ == '__main__':
    main()