from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.PokemonTypeEnum import PokemonType


class FightingTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.FIGHT)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [
                PokemonType.BUG,
                PokemonType.DARK,
                PokemonType.ROCK
            ]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.extend([PokemonType.PSYCHIC, PokemonType.FLYING])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities