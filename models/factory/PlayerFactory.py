from models.Player import Player
from models.factory.PokemonFactory import PokemonFactory


class PlayerFactory:
    """
    Factory to create pre-configured players.
    """

    @staticmethod
    def create_player_1():
        player = Player()
        player.money = 50
        player.add_pokemon(PokemonFactory.create_pikachu())
        player.add_pokemon(PokemonFactory.create_dracaufeu())
        player.add_pokemon(PokemonFactory.create_leviator())
        return player

    @staticmethod
    def create_player_2():
        player = Player()
        player.money = 100
        player.record_round = 5
        player.add_pokemon(PokemonFactory.create_pikachu())
        player.add_pokemon(PokemonFactory.create_leviator())
        return player
