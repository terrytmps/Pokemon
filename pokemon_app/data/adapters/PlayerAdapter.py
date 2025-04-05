from pokemon_app.core.Player import Player
from pokemon_app.data.models.PlayerModel import PlayerModel
from models.Models.PokemonRepository import PokemonRepository
from pokemon_app.core.enum.PokemonName import get_enum_by_value, create_pokemon
from pokemon_app.data.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PlayerAdapter:
    @staticmethod
    def to_model(player: Player) -> PlayerModel:
        """
        Convert an object of domain Player to a PlayerModel.
        """
        if hasattr(player, "id") and player.id:
            player_model = db.session.get(PlayerModel, player.id)
            if player_model is None:
                player_model = PlayerModel()
        else:
            player_model = PlayerModel()

        player_model.name = player.name
        player_model.money = player.money
        player_model.record_round = player.record_round
        player_model.current_pokemon_index = player.current_pokemon

        return player_model

    @staticmethod
    def from_model(player_model: PlayerModel) -> Player:
        """
        Convert an object of PlayerModel to a domain Player.
        """
        player = Player()
        player.id = player_model.id
        player.name = player_model.name
        player.money = player_model.money
        player.record_round = player_model.record_round
        player.current_pokemon = player_model.current_pokemon_index

        for i, pokemon_model in enumerate(player_model.pokemons):
            if i < 6:
                pokemon_bdd = PokemonRepository.find_by_id(pokemon_model.id)
                pokemon_obj = create_pokemon(get_enum_by_value(pokemon_bdd.name))
                pokemon_obj.level_up_to(pokemon_bdd.level)
                player.replace_pokemon(i, pokemon_obj)

        return player
