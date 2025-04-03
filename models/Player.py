from models.Pokemon import Pokemon


class Player:
    def __init__(self):
        self.id: int = 1
        self.name: str = "Player"
        self.money: int = 0
        self._pokemons: list[Pokemon | None] = [None] * 6
        self.record_round: int = 0
        self.current_pokemon: int = -1

    @property
    def pokemons(self):
        return self._pokemons

    def get_current_pokemon(self) -> Pokemon | None:
        if self.current_pokemon == -1:
            return None
        return self._pokemons[self.current_pokemon]

    def set_current_pokemon(self, index):
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
