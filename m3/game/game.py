from abc import ABC, abstractmethod
from util import indent

class Game(ABC):

    @abstractmethod
    def how_many_players(self) -> int:
        pass

    @abstractmethod
    def is_game_over(self) -> bool: 
        pass

    @abstractmethod
    def whose_turn(self) -> int:
        pass

    @abstractmethod
    def get_winner(self) -> int:
        pass

    @abstractmethod
    def get_valid_moves(self) -> list: 
        pass

    @abstractmethod
    def make_move(self, *args): 
        pass

    @abstractmethod
    def string(self, num_indent_spaces: int) -> str:
        pass

    def print(self, num_indent_spaces: int):
        print(self.string(num_indent_spaces))

    def indent(self, num_indent_spaces: int) -> str:
        return indent(num_indent_spaces)
