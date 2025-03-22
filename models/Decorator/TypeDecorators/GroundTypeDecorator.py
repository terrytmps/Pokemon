from models.Decorator.TypeDecorator import TypeDecorator
from models.enum.pokemon_type import PokemonType


class GroundTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.GROUND)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.POISON, PokemonType.ROCK]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append([PokemonType.WATER, PokemonType.GRASS, PokemonType.ICE])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        immunities.append(PokemonType.ELECTRIC)
        return immunities
