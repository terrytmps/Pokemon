from pokemon_app.core.pokemon_type.type_decorator import TypeDecorator
from pokemon_app.core.pokemon_type.utils.pokemon_type_enum import PokemonType


class FlyingTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.FLYING)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend([PokemonType.BUG, PokemonType.FIGHT, PokemonType.GRASS])
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append([PokemonType.ELECTRIC, PokemonType.ICE, PokemonType.ROCK])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        immunities.append(PokemonType.GROUND)
        return immunities
