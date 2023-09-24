from game.game import Game

class TicTacToe(Game):
    def __init__(self, num_players = 2, size = 3):
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
        # print(self)
        self.winner = 0
        self.done = False

    def num_players(self) -> int:
        return self.num_players

    def whose_turn(self) -> int:
        return self.player_to_move

    def is_game_over(self) -> bool: 
        return self.done

    def get_winner(self) -> int:
        return self.winner

    def get_valid_moves(self) -> list: 
        # Return a list of valid moves. 
        # A move is a tuple (row, col). 
        return [(row, col) for row in range(self.size) for col in range(self.size) if self.board[row][col] == 0] 

    def make_move(self, *args): 
        row, col = args[0], args[1]
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

    def string(self, num_indent_spaces: int = 0) -> str:
        s = self.indent(num_indent_spaces)
        s += f'{self.player_to_move}/{self.num_players}\t Game Over: {self.done}\tWinner:{self.winner}'
        for row in range(self.size):
            s += self.indent(num_indent_spaces)
            s += str(self.board[row])
        return s

    
