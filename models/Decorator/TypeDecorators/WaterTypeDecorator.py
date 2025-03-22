from models.Decorator.TypeDecorator import TypeDecorator
from models.enum.pokemon_type import PokemonType


class WaterTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.WATER)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.WATER, PokemonType.FIRE, PokemonType.ICE, PokemonType.STEEL]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.extend([PokemonType.ELECTRIC, PokemonType.GRASS])
        return weaknesses
