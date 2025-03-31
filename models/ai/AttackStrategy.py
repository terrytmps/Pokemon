from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from models.Move import Move

if TYPE_CHECKING:
    from models.Battle import Battle


class AttackStrategy(ABC):
    """Interface for attack strategies"""

    @abstractmethod
    def choose_move(self, battle: 'Battle') -> Move:
        pass



