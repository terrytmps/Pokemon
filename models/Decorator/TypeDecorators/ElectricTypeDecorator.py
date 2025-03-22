from models.Decorator.TypeDecorator import TypeDecorator
from models.enum.pokemon_type import PokemonType


class ElectricTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.ELECTRIC)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.ELECTRIC, PokemonType.FLYING, PokemonType.STEEL]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append(PokemonType.GROUND)
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities