from flask import render_template, Blueprint

from models.enum.move_category import MoveCategory
from models.level.Level import Level
from models.level.Stats import Stat
from models.pokemonType.PokemonTypeEnum import PokemonType
from models.status.StatusEnum import StatusEnum
from models.level.xp_difficulty import XPDifficulty
from models.move import Move
from models.player import Player
from models.pokemon import Pokemon
from models.pokemonType.FireTypeDecorator import FireTypeDecorator
from models.pokemonType.NormalTypeDecorator import NormalTypeDecorator
from models.pokemonType.GrassTypeDecorator import GrassTypeDecorator
from models.pokemonType.WaterTypeDecorator import WaterTypeDecorator

game_controller = Blueprint("game_controller", __name__)

"""
Game endpoints handle the combat part
"""


@game_controller.route("/game")
def game():
    player = Player()
    level = Level(14, XPDifficulty.EASY)
    _pokemon_self = Pokemon(
        "Pikachu",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        10,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100, level.level)
    )

    pokemon_self = FireTypeDecorator(NormalTypeDecorator(_pokemon_self))
    pokemon_self.set_status(StatusEnum.SLEEP)
    pokemon_self.current_hp = 24
    pokemon_self.addMove(
        Move(
            "Tonnerre",
            "A strong electric attack",
            90,
            100,
            PokemonType.ELECTRIC,
            MoveCategory.SPECIAL,
        )
    )
    pokemon_self.addMove(
        Move(
            "Vive-Attaque",
            "A fast attack",
            40,
            100,
            PokemonType.NORMAL,
            MoveCategory.PHYSICAL,
        )
    )
    pokemon_self.addMove(
        Move(
            "Fouet",
            "A status move that lower the defense of the opponent",
            0,
            100,
            PokemonType.DARK,
            MoveCategory.STATUS,
        )
    )
    level = Level(50, XPDifficulty.HARD)
    pokemon_2 = Pokemon(
        "Tortank",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        221,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100, level.level)

    )

    pokemon_2 = WaterTypeDecorator(pokemon_2)
    pokemon_2 = GrassTypeDecorator(pokemon_2)

    player.add_pokemon(pokemon_self)
    player.add_pokemon(pokemon_2)
    player.set_current_pokemon(0)

    level = Level(30, XPDifficulty.HARD)
    _pokemon_op = Pokemon(
        "Salamèche",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
        20,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100, level.level)
    )

    pokemon_op = FireTypeDecorator(_pokemon_op)
    pokemon_op.set_status(StatusEnum.POISON)
    pokemon_op.current_hp = 5

    return render_template("pages/game.html", player=player, pokemon_op=pokemon_op)


"""
Main menu  (where player buy pokemons, etc
"""


@game_controller.route("/")
def menu():
    player = Player()
    level = Level(14, XPDifficulty.EASY)
    pokemon_1 = Pokemon(
        "Pikachu",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        10,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100, level.level)
    )
    pokemon_1 = FireTypeDecorator(pokemon_1)
    pokemon_1 = NormalTypeDecorator(pokemon_1)

    level = Level(50, XPDifficulty.HARD)
    pokemon_2 = Pokemon(
        "Tortank",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png",
        221,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100, level.level)

    )

    pokemon_2 = WaterTypeDecorator(pokemon_2)

    pokemons = [
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_2,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_2,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_2,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_2,
        pokemon_1,
        pokemon_2,
        pokemon_1,
        pokemon_1,
        pokemon_2,
        pokemon_2,
    ]
    player.add_pokemon(pokemon_1)
    return render_template("pages/menu.html", player=player, shop_pokemons=pokemons)
