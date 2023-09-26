
from player.player import play_game
from game.tictactoe import TicTacToe
from game.count import Count
from picker.random import RandomMovePicker
from picker.minimax import MinimaxMovePicker

def main() -> None:
    # play_game(Count(), RandomMovePicker())
    # play_game(Count(goal = 100, max_choice=3), MinimaxMovePicker(max_depth = 20, print_each_minimax=False))
    # play_game(TicTacToe(), RandomMovePicker())
    iterations = 100
    results = ['depth', 'draw', 'x', 'o']
    for max_depth in range(1, 3):
        print('max_depth', max_depth)
        x = 0
        o = 0
        draw = 0
        for j in range(iterations):
            print('iteration', j)
            game = TicTacToe()
            play_game(game, MinimaxMovePicker(max_depth = max_depth, print_each_minimax=False), print_each_move=False)
            if game.get_winner() == 0:
                draw += 1
            elif game.get_winner() == 1:   
                x += 1
            else:
                o += 1
        results.append([max_depth, draw, x, o])

    for row in results:
        print(row)
    # print(results)

if __name__ == '__main__':
    main()