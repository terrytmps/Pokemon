from flask import jsonify
from typing_extensions import Optional

from pokemon_app.core.battle import Battle
from pokemon_app.data.repositories.player_repository import PlayerRepository
from pokemon_app.core.player import Player
from pokemon_app.core.pokemon import Pokemon
from pokemon_app.core.round_generator import RoundGenerator

player = Player()
battle: Battle
pokemon_op = None


def get_current_battle():
    return battle


def init_battle():
    global player
    player = PlayerRepository().find_by_id(1)
    global pokemon_op
    pokemon_op = RoundGenerator.get_instance().reset()
    pokemon_op = RoundGenerator.get_instance().generate_round()
    return None


def create_battle():
    """create a battle with the player pokemon and a random pokemon"""
    global battle
    battle = Battle(player.get_current_pokemon(), pokemon_op)
    return battle


def game_perform_attack(attack: int):
    """perform the attack of the player and return the pokemon new stats"""

    player_selected_move = battle.player_pokemon.get_moves()[attack]
    opponent_selected_move = battle.choose_opponent_move()

    [only_one_attack, player_attacked_first] = battle.battle_turn(
        player_selected_move,
        opponent_selected_move,
    )

    return jsonify(
        [
            only_one_attack,
            player_attacked_first,
            battle.player_pokemon.to_dict(),
            battle.opponent_pokemon.to_dict(),
        ]
    )


def game_perform_change(position: int):
    """change the pokemon of the player and return the pokemon new stats"""
    is_dead = battle.player_pokemon.get_current_hp() <= 1

    player.set_current_pokemon(int(position) - 1)
    battle.player_pokemon = player.get_current_pokemon()

    # if the change happens because your Pokemon is dead, the opponent won't attack you directly
    if not is_dead:
        opponent_selected_move = battle.choose_opponent_move()
        battle.battle_turn(None, opponent_selected_move)

    return [battle.player_pokemon.to_dict(), battle.opponent_pokemon.to_dict()]


def forfet():
    """forfet the game and return to the menu"""
    battle.gave_up(player)
    PlayerRepository.save(player)


def is_winner_back() -> Pokemon | bool | None:
    """look if there a winner
    - if player won send next pokemon
    - if player won not other pokemon send true
    - if no one win return false
    - if player loose return false
    """
    pokemon: Optional[Pokemon] = battle.get_battle_winner(player)
    # if optional is empty then no one won and return false
    if pokemon is None:
        return False
    if pokemon is True:
        return True
    if pokemon.name == battle.player_pokemon.name:
        global pokemon_op
        pokemon_op = RoundGenerator.get_instance().generate_round()
        create_battle()
        return pokemon_op
    return False


def battle_log_get():
    """Return the last battle log"""
    return battle.get_battle_log()
