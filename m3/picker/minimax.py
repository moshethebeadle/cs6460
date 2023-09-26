from game.game import Game
from picker.picker import AbstractMovePicker
from util import indent
import copy as cp
import random

def evaluate(game: Game): 
    if game.get_winner() == 2:
        return -1
    if game.get_winner() == 1:
        return 1
    return 0

class MinimaxMovePicker(AbstractMovePicker): 
    def __init__(self, max_depth = 2, print_each_minimax = True, prune = True):
        if max_depth <= 0:
            raise ValueError('max depth has to be > 0')
        self.max_depth = max_depth
        self.print_each_minimax = print_each_minimax
        self.prune = prune
    
    def pick_move(self, game: Game):
        _, mv = self.minimax(game, 0, -float('inf'), float('inf'))
        return mv
        
    # returns best_score, best_move (or None)
    def minimax(self, game: Game, depth: int, alpha: int, beta: int):
        if game.how_many_players() > 2:
            raise ValueError(f"Can't do minimax with more than 2 players ({self.num_players})")

        if self.print_each_minimax:
            print(f'{indent(depth)}minimax state: ', game.string(depth))
            
        # If we've reached the maximum depth or the game is over, return the score. 
        if depth == self.max_depth or game.is_game_over(): 
            # print(f"{self.indent()} player {self.player_to_move} detects that the winner is player {self.winner}")
            val = evaluate(game)
            if self.print_each_minimax: # or val != 0:
                print(f"{indent(depth)}Eval: {val}")
            return val, None 

        # Initialize the best score and best move. 
        # Player 1 wants to maximize the score. 
        # Player 2 wants to minimize the score. 
        sign = 1 if game.whose_turn() == 1 else -1
        best_score = -float('inf') * sign # negative infinity for player 1, positive infinity for player 2
        best_moves = []

        # Try all possible moves. 
        for move in game.get_valid_moves():
            if self.print_each_minimax:
                print(f"{indent(depth)}evaluating move {move}") 
            # deep copy the game and make the move.
            next_game = cp.deepcopy(game)
            next_game.make_move(move) 
            score, _ = self.minimax(next_game, depth + 1, alpha, beta) 
            if self.print_each_minimax: # or score != 0:
                print(f"{indent(depth)}player {game.whose_turn()}: move {move} returned score {score}")

            # Update the best score and best move. 
            # TODO - randomly pick a move out of moves that are all equal?
            if sign * score == sign * best_score: 
                if self.print_each_minimax:
                    print(f"{indent(depth)}same move: {move} \t moves: {best_moves}")
                best_moves.append(move)
            if sign * score > sign * best_score: 
                if self.print_each_minimax:
                    print(f"{indent(depth)}better move: {move}")
                best_score = score 
                best_moves = [move]

            # Update the alpha/beta values 
            if game.whose_turn() == 1: 
                alpha = max(alpha, best_score) 
            else: 
                beta = min(beta, best_score) 
 
            # Alpha Beta Pruning condition 
            if beta <= alpha: 
                if self.print_each_minimax:
                    print(f"{indent(depth)}Pruning: {beta} <= {alpha}")
                if self.prune:
                    break 
                else:
                    if self.print_each_minimax:
                        print(f"{indent(depth)}NOT Pruning due to prune = False")

        return best_score, best_moves[random.randint(0, len(best_moves)-1)]
