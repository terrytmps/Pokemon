from models.Pokemon import Pokemon

"""
Decorator that allow to add multiple type to a pokemon wihtout the need to change the code of pokemon for each possible type
"""
class TypeDecorator(Pokemon):

    def __init__(self, pokemon: Pokemon):
        super().__init__(
            pokemon.name,
            pokemon.sprite_url,
            pokemon.price,
            pokemon.get_level_object(),
            pokemon.stat,
        )
        self._component = pokemon

    # Pattern Decorator
    def get_types(self):
        return self._component.get_types()

    def get_resistances(self):
        return self._component.get_resistances()

    def get_weaknesses(self):
        return self._component.get_weaknesses()

    def get_immunity(self):
        return self._component.get_immunity()

    @property
    def first_type(self):
        types = self.get_types()
        if types:
            return types[0]
        return None

    @property
    def second_type(self):
        types = self.get_types()
        if len(types) > 1:
            return types[1]
        return None
