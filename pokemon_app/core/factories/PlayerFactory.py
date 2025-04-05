from pokemon_app.core.Player import Player
from pokemon_app.core.factories.PokemonFactory import PokemonFactory


class PlayerFactory:
    """
    Factory to create pre-configured players.
    """

    @staticmethod
    def create_player_1():
        player = Player()
        player.name = "Gimmighoul"
        pokemon_self = PokemonFactory.create_tyranocif()
        pokemon_self.level_up_to(100)
        pokemon_self_second = PokemonFactory.create_aquali()
        pokemon_self_second.level_up_to(10)
        player.add_pokemon(pokemon_self_second)
        player.add_pokemon(pokemon_self)
        player.set_current_pokemon(0)
        player.money = 100
        return player

    @staticmethod
    def create_player_2():
        player = Player()
        player.money = 100
        player.record_round = 5
        player.add_pokemon(PokemonFactory.create_pikachu())
        player.add_pokemon(PokemonFactory.create_leviator())
        return player
