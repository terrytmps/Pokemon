from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from pokemon_app.core.Move import Move

if TYPE_CHECKING:
    from pokemon_app.core.Battle import Battle


class AttackStrategy(ABC):
    """Interface for attack strategies"""

    @abstractmethod
    def choose_move(self, battle: "Battle") -> Move:
        pass
