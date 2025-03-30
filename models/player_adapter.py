from models.player_model import PlayerModel
from models.pokemon_model import PokemonModel
from models.Database import DatabaseSingleton
from models.Player import Player


class PlayerDBAdapter:
    """
    Adaptateur pour convertir les objets Player en objets PlayerModel pour la base de données
    """

    def __init__(self):
        self.db = DatabaseSingleton.get_instance().get_db()

    def save_player(self, player, player_id=None):
        """
        Sauvegarde un objet Player dans la base de données
        """
        # Si le joueur existe déjà on le récupère
        if player_id:
            player_model = PlayerModel.query.get(player_id)
            if not player_model:
                player_model = PlayerModel(id=player_id)
        else:
            player_model = PlayerModel()

        player_model.money = player.money
        player_model.record_round = player.record_round
        player_model.current_pokemon = player.current_pokemon

        self.db.session.add(player_model)
        self.db.session.commit()

        # Sauvegarde des Pokémon (supprimer les anciens Pokémon)
        PokemonModel.query.filter_by(player_id=player_model.id).delete()

        for i, pokemon in enumerate(player.pokemons):
            if pokemon is not None:
                pokemon_model = PokemonModel(
                    name=pokemon.name, player_id=player_model.id, position=i
                )
                self.db.session.add(pokemon_model)

        self.db.session.commit()
        return player_model.id

    def load_player(self, player_id):
        """
        Charge un joueur depuis la base de données
        """
        from models.factory.PokemonFactory import PokemonFactory

        player_model = PlayerModel.query.get(player_id)
        if not player_model:
            return None

        player = Player()
        player.money = player_model.money
        player.record_round = player_model.record_round
        player.current_pokemon = player_model.current_pokemon

        pokemon_models = (
            PokemonModel.query.filter_by(player_id=player_id)
            .order_by(PokemonModel.position)
            .all()
        )

        player._pokemons = [None] * 6

        factory = PokemonFactory()

        for pokemon_model in pokemon_models:
            # Créer un Pokémon en fonction du nom
            if pokemon_model.name == "Pikachu":
                pokemon = factory.create_pikachu()
            else:
                pokemon = factory.create_dracaufeu()

            player._pokemons[pokemon_model.position] = pokemon

        return player
