from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.pokemon_type import PokemonType


class PoisonTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.POISON)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.FIGHT, PokemonType.POISON, PokemonType.BUG, PokemonType.GRASS]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append([PokemonType.GROUND, PokemonType.PSYCHIC])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        return immunities