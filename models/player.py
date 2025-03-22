from models.pokemon import Pokemon


class Player:
    def __init__(self):
        self.money = 0
        self._pokemons = [None] * 6
        self.record_round = 0
        self.current_pokemon = -1

    @property
    def pokemons(self):
        return self._pokemons

    def get_current_pokemon(self):
        if self.current_pokemon == -1:
            return None
        return self._pokemons[self.current_pokemon]

    def set_current_pokemon(self, index):
        print("set" + str(index))
        assert 0 <= index < 6
        self.current_pokemon = index

    def add_pokemon(self, pokemon: Pokemon) -> bool:
        """
        Add a pokemon to the team only if there is a free slot
        """
        for i in range(6):
            if self._pokemons[i] is None:
                if i == 0:
                    self.current_pokemon = 0
                self._pokemons[i] = pokemon
                return True
        return False

    def replace_pokemon(self, index, pokemon):
        """
        Replace a pokemon in the team
        """
        assert 0 <= index < 6
        self._pokemons[index] = pokemon
