from models.PokemonType.TypeDecorator import TypeDecorator
from models.enum.pokemon_type import PokemonType


class FireTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.FIRE)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [
                PokemonType.FIRE,
                PokemonType.GRASS,
                PokemonType.ICE,
                PokemonType.BUG,
                PokemonType.STEEL,
            ]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.extend([PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities