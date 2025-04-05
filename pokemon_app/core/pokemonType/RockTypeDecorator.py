from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.utils.PokemonTypeEnum import PokemonType


class RockTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.ROCK)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [
                PokemonType.NORMAL,
                PokemonType.FLYING,
                PokemonType.POISON,
                PokemonType.FIRE,
            ]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append(
            [
                PokemonType.WATER,
                PokemonType.GRASS,
                PokemonType.FIGHT,
                PokemonType.GROUND,
                PokemonType.STEEL,
            ]
        )
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities
