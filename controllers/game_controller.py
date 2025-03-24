from flask import render_template, Blueprint

from models.enum.MoveCategory import MoveCategory
from models.level.Level import Level
from models.level.Stats import Stat
from models.pokemonType.utils.PokemonTypeEnum import PokemonType
from models.status.StatusEnum import StatusEnum
from models.level.XpDifficulty import XPDifficulty
from models.Move import Move
from models.Player import Player
from models.Pokemon import Pokemon
from models.pokemonType.FireTypeDecorator import FireTypeDecorator
from models.pokemonType.NormalTypeDecorator import NormalTypeDecorator
from models.pokemonType.GrassTypeDecorator import GrassTypeDecorator
from models.pokemonType.WaterTypeDecorator import WaterTypeDecorator

game_controller = Blueprint("game_controller", __name__)


@game_controller.route("/game")
def game():
    """
    Game endpoints handle the combat part
    """

    player = Player()
    stat = Stat(10, 1, 1, 1, 1, 1,
                100, 100, 100, 100, 100, 100)
    tonnerreMove = Move(
        "Tonnerre",
        "A strong electric attack",
        90,
        100,
        PokemonType.ELECTRIC,
        MoveCategory.SPECIAL,
    )
    viveAttaqueMove = Move(
        "Vive-Attaque",
        "A fast attack",
        40,
        100,
        PokemonType.NORMAL,
        MoveCategory.PHYSICAL,
    )

    pokemon_self = Pokemon.Builder() \
        .set_name("Pikachu") \
        .set_img(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png") \
        .set_level(10, XPDifficulty.EASY) \
        .set_stat(stat) \
        .set_price(10) \
        .set_type(PokemonType.ELECTRIC) \
        .set_moves(tonnerreMove) \
        .set_moves(viveAttaqueMove) \
        .build()

    pokemon_self.set_status(StatusEnum.SLEEP)
    pokemon_self.current_hp = 24

    stat = Stat(1, 1, 1, 1, 1, 1,
                100, 100, 100, 100, 100, 100)
    pokemon_2 = Pokemon.Builder() \
        .set_name("Tortank") \
        .set_img(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png") \
        .set_level(35, XPDifficulty.HARD) \
        .set_stat(stat) \
        .set_price(110) \
        .set_type(PokemonType.WATER) \
        .set_type(PokemonType.NORMAL) \
        .set_moves(viveAttaqueMove) \
        .build()

    player.add_pokemon(pokemon_self)
    player.add_pokemon(pokemon_2)
    player.set_current_pokemon(0)

    pokemon_op = Pokemon.Builder() \
        .set_name("Salamèche") \
        .set_img(
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png") \
        .set_level(23, XPDifficulty.HARD) \
        .set_stat(stat) \
        .set_price(20) \
        .set_type(PokemonType.FIRE) \
        .set_type(PokemonType.DRAGON) \
        .build()


    pokemon_op.set_status(StatusEnum.POISON)
    pokemon_op.current_hp = 5

    return render_template("pages/game.html", player=player, pokemon_op=pokemon_op)


@game_controller.route("/")
def menu():
    """
    Main menu  (where player buy pokemons, etc
    """
    player = Player()
    level = Level(14, XPDifficulty.EASY)
    pokemon_1 = Pokemon(
        "Pikachu",
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        10,
        level,
        Stat(1, 1, 1, 1, 1, 1,
             100, 100, 100, 100, 100, 100)
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
             100, 100, 100, 100, 100, 100)

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
