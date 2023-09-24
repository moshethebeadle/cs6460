from picker.picker import AbstractMovePicker
from game.game import Game

def play_game(game: Game, move_picker: AbstractMovePicker, print_each_move = True):
    print('\nStarting Game!')
    while True:
        if game.is_game_over():
            if game.get_winner() == 0:
                print("It's a Draw!")
            else:
                print('Winner: ', game.get_winner())
            return
        
        mv = move_picker.pick_move(game)

        if print_each_move:
            print(f'*Player {game.whose_turn()} chose move {mv}: ')

        game.make_move(mv)

        if print_each_move:
            game.print(0)

