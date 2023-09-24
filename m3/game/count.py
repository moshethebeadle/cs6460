from game.game import Game

class Count(Game):
    def __init__(self, goal: int = 5):
        self.turn = 1
        self.goal = goal
        self.count = 0
        self.winner = None

    def how_many_players(self) -> int:
        return 2

    def is_game_over(self) -> bool: 
        game_over = self.count >= self.goal
        # print(f'Count: {self.count} >= {self.goal} = {game_over}')
        return game_over

    def whose_turn(self) -> int:
        return self.turn

    def get_winner(self) -> int:
        return self.winner

    def get_valid_moves(self) -> list[tuple]: 
        return [1, 2]

    def make_move(self, *args): 
        self.count += args[0]
        self.game_over = self.count >= self.goal
        if self.game_over:
            self.winner = self.turn
        else:
            self.turn = 3 - self.turn

    def string(self, num_indent_spaces: int) -> str:
        return self.indent(num_indent_spaces) + f'Count: {self.count}\tTurn: {self.turn} \t Winner:{self.winner}'

