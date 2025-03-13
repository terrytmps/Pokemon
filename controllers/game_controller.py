from flask import render_template, Blueprint

from models.enum.move_category import MoveCategory
from models.enum.pokemon_type import PokemonType
from models.enum.xp_difficulty import XPDifficulty
from models.move import Move
from models.pokemon import Pokemon

game_controller = Blueprint("game_controller", __name__)

@game_controller.route("/")
def game():
    pokemon_self = Pokemon("Pikachu", 12, 57, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
                        XPDifficulty.EASY, PokemonType.ELECTRIC, PokemonType.FIRE)
    pokemon_self.current_hp = 24
    pokemon_self.addMove(Move("Tonnerre", "A strong electric attack", 90, 100, PokemonType.ELECTRIC, MoveCategory.SPECIAL))
    pokemon_self.addMove(Move("Vive-Attaque", "A fast attack", 40, 100, PokemonType.NORMAL, MoveCategory.PHYSICAL))
    pokemon_self.addMove(Move("Fouet", "A status move that lower the defense of the opponent", 0, 100, PokemonType.DARK, MoveCategory.STATUS))

    pokemon_op = Pokemon("Salamèche", 10, 30, "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
                         XPDifficulty.EASY, PokemonType.FIRE, PokemonType.NONE)
    pokemon_op.current_hp = 5
    return render_template("pages/game.html", pokemon_self=pokemon_self, pokemon_op=pokemon_op)
