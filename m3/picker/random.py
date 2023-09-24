from picker.picker import AbstractMovePicker
import random

class RandomMovePicker(AbstractMovePicker):

    def pick_move(self, game):
        moves = game.get_valid_moves()
        return random.choice(moves)
        
