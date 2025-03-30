from flask import render_template, Blueprint

from models.factory.PokemonFactory import PokemonFactory
from models.player_adapter import PlayerDBAdapter


shop_controller = Blueprint("shop_controller", __name__)


@shop_controller.route("/")
def menu():
    """
    Main menu  (where player buy Pokémon, etc.)
    """
    player = PlayerDBAdapter().get_unique_player()
    pokemons = PokemonFactory.get_shop_pokemons()
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)
