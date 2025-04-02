from models.Player import Player
from models.factory.PokemonFactory import PokemonFactory


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
        player.add_pokemon(pokemon_self)
        player.add_pokemon(pokemon_self_second)
        player.set_current_pokemon(1)
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
