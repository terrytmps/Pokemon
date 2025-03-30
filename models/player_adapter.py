from models.enum.PokemonName import PokemonName, pokemon_factory_methods
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

        player_model.name = player.name
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
        player.name = player_model.name
        player.money = player_model.money
        player.record_round = player_model.record_round
        player.current_pokemon = player_model.current_pokemon

        pokemon_models = (
            PokemonModel.query.filter_by(player_id=player_id)
            .order_by(PokemonModel.position)
            .all()
        )

        player._pokemons = [None] * 6

        for pokemon_model in pokemon_models:
            try:
                pokemon_name = PokemonName(pokemon_model.name)
                pokemon = pokemon_factory_methods[pokemon_name]()
            except ValueError:
                raise ValueError(f"Unknown Pokémon name: {pokemon_model.name}")

            player._pokemons[pokemon_model.position] = pokemon

        return player

    def get_unique_player(self):
        """
        Récupère le joueur unique depuis la base de données
        S'il n'existe pas, crée un nouveau joueur et le retourne

        Returns:
            Player: L'objet Player unique (existant ou nouveau)
        """
        player_model = PlayerModel.query.first()

        if player_model:
            return self.load_player(player_model.id)
        else:
            from models.factory.PokemonFactory import PokemonFactory

            player = Player()
            player.name = "Terry"

            pokemon_self = PokemonFactory.create_tyranocif()
            pokemon_self.level_up_to(100)
            pokemon_self_second = PokemonFactory.create_aquali()
            player.add_pokemon(pokemon_self)
            player.add_pokemon(pokemon_self_second)
            player.set_current_pokemon(1)

            player_id = self.save_player(player)

            return self.load_player(player_id)

    def update_player(self, new_player):
        """
        Met à jour les informations d'un joueur existant dans la base de données.
        """
        player_model = PlayerModel.query.first()

        player_model.name = new_player.name
        player_model.money = new_player.money
        player_model.record_round = new_player.record_round
        player_model.current_pokemon = new_player.current_pokemon

        self.db.session.commit()

        PokemonModel.query.filter_by(player_id=player_model.id).delete()

        for i, pokemon in enumerate(new_player.pokemons):
            if pokemon is not None:
                pokemon_model = PokemonModel(
                    name=pokemon.name, player_id=player_model.id, position=i
                )
                self.db.session.add(pokemon_model)

        self.db.session.commit()
