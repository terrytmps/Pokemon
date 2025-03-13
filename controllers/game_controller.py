from flask import render_template, Blueprint

from models.enum.pokemon_type import PokemonType
from models.enum.xp_difficulty import XPDifficulty
from models.pokemon import Pokemon

game_controller = Blueprint("game_controller", __name__)

@game_controller.route("/")
def game():
    pokemon_self = Pokemon("Pikachu", 12, 57, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
                        XPDifficulty.EASY, PokemonType.ELECTRIC, PokemonType.NONE)
    return render_template("pages/game.html", pokemon_self=pokemon_self)
