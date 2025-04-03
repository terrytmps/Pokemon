from models.Database import DatabaseSingleton
from models.Player import Player
from models.Models.PlayerModel import PlayerModel
from models.Models.PokemonRepository import PokemonRepository
from models.enum.PokemonName import get_enum_by_value, create_pokemon

db = DatabaseSingleton.get_instance().get_db()


class PlayerRepository:
    @staticmethod
    def save(player: Player) -> int:
        """
        Save a Player to the database
        """
        player_id = getattr(player, "id", None)
        player_model = None

        if player_id:
            player_model = PlayerModel.query.get(player_id)

        if player_model is None:
            player_model = PlayerModel(
                name=player.name,
                money=player.money,
                record_round=player.record_round,
                current_pokemon_index=player.current_pokemon,
            )
            db.session.add(player_model)
            db.session.flush()
        else:
            player_model.name = player.name
            player_model.money = player.money
            player_model.record_round = player.record_round

        PokemonRepository().delete_all_pokemons_player(player_id=player_model.id)

        # Save pokemons
        if hasattr(player, "_pokemons"):
            for i, pokemon in enumerate(player.pokemons):
                if pokemon is not None:
                    pokemon_id = PokemonRepository.save(pokemon, player_model.id)

        db.session.commit()

        # if the player was new, set the id
        if not hasattr(player, "id"):
            player.id = player_model.id

        return player_model.id

    @staticmethod
    def find_by_id(player_id: int) -> Player | None:
        """
        Load a Player from the database
        """
        player_model = PlayerModel.query.get(player_id)
        if not player_model:
            return None

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
