from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.utils.PokemonTypeEnum import PokemonType


class PsychicTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.PSYCHIC)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend([PokemonType.FIGHT, PokemonType.PSYCHIC])
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.extend([PokemonType.BUG, PokemonType.GHOST, PokemonType.DARK])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities