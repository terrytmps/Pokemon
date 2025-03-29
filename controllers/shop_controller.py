from flask import render_template
from flask.sansio.blueprints import Blueprint

from models.Player import Player
from models.factory.PokemonFactory import PokemonFactory

shop_controller = Blueprint("game_controller", __name__)


@shop_controller.route("/")
def menu():
    """
    Main menu  (where player buy pokemons, etc
    """
    player = Player()
    pokemons = PokemonFactory.get_shop_pokemons()
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)
