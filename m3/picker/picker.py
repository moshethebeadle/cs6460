
from abc import ABC, abstractmethod

from game.game import Game

class AbstractMovePicker(ABC):
    @abstractmethod
    def pick_move(self, game: Game) -> any:
        pass