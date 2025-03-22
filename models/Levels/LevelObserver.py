from abc import ABC


class LevelObserver(ABC):
    def on_level_up(self, pokemon, old_level: int, new_level: int):
        """
        Méthode appelée quand un Pokémon gagne un niveau

        TODO: Implémenter la logique de notification

        """
        pass
