from models.pokemonType.TypeDecorator import TypeDecorator
from models.pokemonType.pokemon_type import PokemonType


class GhostTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append(PokemonType.GHOST)
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(
            [PokemonType.POISON, PokemonType.BUG]
        )
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append([PokemonType.GHOST, PokemonType.DARK])
        return weaknesses

    def get_immunity(self):
        immunities = self._component.get_immunity()
        immunities.append([PokemonType.NORMAL, PokemonType.FIGHT])
        return immunities