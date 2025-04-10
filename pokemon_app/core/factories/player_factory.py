from pokemon_app.core.player import Player
from pokemon_app.core.factories.pokemon_factory import PokemonFactory


class PlayerFactory:
    """
    Factory to create pre-configured players.
    """

    @staticmethod
    def create_player_tests():
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
        player.id = 2
        return player

    @staticmethod
    def create_player_prod():
        player = Player()
        player.name = "Devastator"
        player.add_pokemon(PokemonFactory.create_pikachu())
        player.set_current_pokemon(0)
        player.money = 60
        player.record_round = 0
        player.id = 1
        return player
