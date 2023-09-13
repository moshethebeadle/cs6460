
import random

class GamePlayer:
    def __init__(self, print_each_move = False):
        self.print_each_move = print_each_move

    def pick_move(self, moves):
        pass

    def play_game(self, game):
        print('Starting Game!')
        while True:
            if game.is_game_over():
                if game.get_winner() == 0:
                    print("Cat's Game!")
                else:
                    print('Winner: ', game.get_winner())
                return
            
            moves = game.get_valid_moves()
            
            mv = self.pick_move(moves)
            
            game.make_move(*mv)
            if self.print_each_move:
                self.print(game)

    def print(self, game):
        game.print()


class RandomGamePlayer(GamePlayer):
    def __init__(self, print_each_move = False):
        super().__init__(print_each_move)

    def pick_move(self, moves):
        return random.choice(moves)
        
