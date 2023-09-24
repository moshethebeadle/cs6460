
from player.player import play_game
from game.tictactoe import TicTacToe
from game.count import Count
from picker.random import RandomMovePicker
from picker.minimax import MinimaxMovePicker

def main() -> None:
    play_game(Count(), RandomMovePicker())
    play_game(Count(goal = 2), MinimaxMovePicker(max_depth = 5))
    play_game(TicTacToe(), RandomMovePicker())
    play_game(TicTacToe(), MinimaxMovePicker(max_depth = 5))

if __name__ == '__main__':
    main()