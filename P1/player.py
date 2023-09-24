
import random
import util

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
            
            mv = self.pick_move(game)
            
            game.make_move(*mv)
            if self.print_each_move:
                self.print(game)

    def print(self, game):
        game.print()


class RandomGamePlayer(GamePlayer):
    def __init__(self, print_each_move = True):
        super().__init__(print_each_move)

    def pick_move(self, game):
        moves = game.get_valid_moves()
        return random.choice(moves)
        
class MinimaxGamePlayer(GamePlayer): 
    def __init__(self, print_each_move = True, max_depth = 2, print_each_minimax = False):
        super().__init__(print_each_move)
        if max_depth <= 0:
            raise ValueError('max depth has to be > 0')
        self.max_depth = max_depth
        self.depth = 0
        self.print_each_minimax = print_each_minimax

    # override
    def pick_move(self, game):
        _, mv = self.minimax()
        print(f'Player {self.player_to_move} chose move {mv}: ')
        return mv
        
    def evaluate(game): 
        if game.get_winner() == 2:
            return -1
        if game.get_winner() == 1:
            return 1
        return 0

    # returns best_score, best_move (or None)
    def minimax(self):
        if self.num_players > 2:
            raise ValueError(f"Can't do minimax with more than 2 players ({num_players})")

        if self.print_each_minimax:
            print('minimax state: ', game.game_state_str())
            
        # If we've reached the maximum depth or the game is over, return the score. 
        if self.depth == self.max_depth or game.is_game_over(): 
            # print(f"{self.indent()} player {self.player_to_move} detects that the winner is player {self.winner}")
            val = self.evaluate()
            if self.print_each_minimax or val != 0:
                print(f"{util.indent()} Eval: {val}")
            return val, None 

        # Initialize the best score and best move. 
        # Player 1 wants to maximize the score. 
        # Player 2 wants to minimize the score. 
        sign = 1 if self.player_to_move == 1 else -1
        best_score = -float('inf') * sign # negative infinity for player 1, positive infinity for player 2
        best_move = None 

        # Try all possible moves. 
        for move in self.get_valid_moves(): 
            new_state = self.copy()  # copy() is a helper method that clones the current state. 
            new_state.make_move(*move) 
            new_state.depth += 1
            score, _ = new_state.minimax() 
            if self.print_each_minimax or score != 0:
                print(game_state_str(new_state))
                print(f"{self.indent()} player {self.player_to_move}: move {move} returned score {score}")

            # Update the best score and best move. 
            # TODO - randomly pick a move out of moves that are all equal?
            if sign * score > sign * best_score: 
                if self.print_each_minimax:
                    print(f"{self.indent()} player {self.player_to_move} updates best move to: {move}")
                best_score = score 
                best_move = move 

        return best_score, best_move 

    def indent(self):
        return indent(self.depth)
    
    # Update print() to use a toString method
    def game_state_str(self):
        s = self.indent()
        s += f'{self.player_to_move}/{self.num_players}\t Game Over: {self.done}\tWinner:{self.winner}'
        for row in range(self.size):
            s += self.indent()
            s += str(self.board[row])
        return s  
    
    def print(self):
        print(self.game_state_str())