class Game:
    def is_game_over(self): 
        pass

    def get_winner(self):
        pass

    def get_valid_moves(self): 
        pass

    def make_move(self, row, col): 
        pass

    def print(self):
        pass

class TicTacToe(Game):
    def __init__(self, num_players = 2, size = 3, print_each_move = True):
        # We represent the Tic-Tac-Toe board as a 3x3 array. 
        # We use 0 to represent an empty square, 1 for Player 1's piece, and 2 for Player 2's piece. 
        self.board = []
        for row in range(size):
            self.board.append([])
            for col in range(size):
                self.board[row].append(0)
        # Player 1 goes first. 
        self.player_to_move = 1 # random.choice(list(range(1, num_players+1)))
        self.num_players = num_players
        self.size = size
        self.print_each_move = print_each_move
        # print(self)
        self.winner = 0
        self.done = False

    def is_game_over(self): 
        return self.done

    def get_winner(self):
        return self.winner

    def get_valid_moves(self): 
        # Return a list of valid moves. 
        # A move is a tuple (row, col). 
        return [(row, col) for row in range(self.size) for col in range(self.size) if self.board[row][col] == 0] 

    def make_move(self, row, col): 
        # Make a move at the specified location. 
        # This assumes that the move is valid. 
        assert self.board[row][col] == 0 
        self.board[row][col] = self.player_to_move 
        # Switch the player to move. 
        self.player_to_move += 1
        if self.player_to_move > self.num_players:
            self.player_to_move = 1
        done, winner = self.get_status()
        self.winner = winner
        self.done = done

    def get_status(self):
        # Quick check
        for player in range(1, self.num_players + 1): 
            for row in range(self.size): 
                if all(self.board[row][col] == player for col in range(self.size)): 
                    return True, player 
            for col in range(self.size): 
                if all(self.board[row][col] == player for row in range(self.size)): 
                    return True, player 
            if all(self.board[i][i] == player for i in range(self.size)): 
                return True, player 
            if all(self.board[i][self.size-1-i] == player for i in range(self.size)): 
                return True, player 

        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return False, 0 # Game not over yet
            
        return True, 0 # Cat's game

    def print(self):
        print(f'{self.player_to_move}/{self.num_players}')
        for row in range(self.size):
            print(self.board[row])

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
                    print('Game over. Winner: ', game.get_winner())
                return
            
            moves = game.get_valid_moves()
            
            mv = self.pick_move(moves)
            
            game.make_move(*mv)
            if self.print_each_move:
                self.print(game)

    def print(self, game):
        game.print()



import random

class RandomGamePlayer(GamePlayer):
    def __init__(self, print_each_move = False):
        super().__init__(print_each_move)

    def pick_move(self, moves):
        return random.choice(moves)
        


def main() -> None:
    print("hi")

    game = TicTacToe(num_players = 2, size = 3, print_each_move = True)
    player = RandomGamePlayer(print_each_move = True)
    player.play_game(game)

if __name__ == '__main__':
    main()