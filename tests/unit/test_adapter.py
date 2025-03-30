import pytest
from flask import Flask
from models.Database import DatabaseSingleton
from models.Player import Player
from models.factory.PlayerFactory import PlayerFactory
from models.player_adapter import PlayerDBAdapter
from models.factory.PokemonFactory import PokemonFactory


@pytest.fixture(scope="module")
def test_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db_singleton = DatabaseSingleton.get_instance(app)
    db = db_singleton.get_db()
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


class TestPlayerDBAdapter:
    @pytest.fixture(autouse=True)
    def setup(self, test_app):
        self.app = test_app
        self.adapter = PlayerDBAdapter()

    def test_save_and_load_player(self):
        player = PlayerFactory().create_player_2()

        factory_pokemon = PokemonFactory()

        player._pokemons = [None] * 6
        player._pokemons[0] = factory_pokemon.create_pikachu()
        player._pokemons[1] = factory_pokemon.create_dracaufeu()

        player_id = self.adapter.save_player(player)
        assert (
            player_id is not None
        ), "L'identifiant du joueur sauvegardé ne doit pas être None"

        loaded_player = self.adapter.load_player(player_id)

        assert loaded_player

        assert loaded_player is not None, "Le joueur chargé ne doit pas être None"
        assert loaded_player.money == 100, "La somme d'argent doit être identique"
        assert (
            loaded_player.record_round == 5
        ), "Le record de rounds doit être identique"
        assert (
            loaded_player.current_pokemon == 0
        ), "Le Pokémon courant doit être identique"

        assert (
            loaded_player._pokemons[0] is not None
        ), "Le Pokémon à la position 0 ne doit pas être None"
        assert (
            loaded_player._pokemons[0].name == "Pikachu"
        ), "Le Pokémon à la position 0 doit être un Pikachu"
        assert (
            loaded_player._pokemons[1] is not None
        ), "Le Pokémon à la position 1 ne doit pas être None"
        assert (
            loaded_player._pokemons[1].name == "Dracaufeu"
        ), "Le Pokémon à la position 1 doit être un Dracaufeu"
