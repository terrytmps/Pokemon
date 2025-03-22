from models.Decorator.Component import Component
from typing import List
from models.Observer.LevelObserver import LevelObserver
from models.pokemon import Pokemon


class TypeDecorator(Pokemon):

    def __init__(self, pokemon: Pokemon):
        super().__init__(
            pokemon.name,
            pokemon.level,
            pokemon.max_hp,
            pokemon.sprite_url,
            pokemon._xp_difficulty,
            pokemon.price,
        )
        self._component = pokemon

    # Pattern Decorator
    def get_types(self):
        return self._component.get_types()

    def get_resistances(self):
        return self._component.get_resistances()

    def get_weaknesses(self):
        return self._component.get_weaknesses()

    @property
    def first_type(self):
        types = self.get_types()
        if types:
            return types[0]
        return None

    @property
    def second_type(self):
        types = self.get_types()
        if len(types) > 1:
            return types[1]
        return None
