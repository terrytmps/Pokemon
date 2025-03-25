from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.utils.PokemonTypeEnum import PokemonType


class IceTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.ICE)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.ICE]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append([PokemonType.STEEL, PokemonType.FIRE, PokemonType.FIGHT, PokemonType.ROCK])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities
