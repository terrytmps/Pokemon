from flask import jsonify

from models.Battle import Battle
from models.Player import Player
from models.RoundGenerator import RoundGenerator
from models.factory.PokemonFactory import PokemonFactory

player = Player()
pokemon_self = PokemonFactory.create_chrysacier()
pokemon_self_second = PokemonFactory.create_aquali()
player.add_pokemon(pokemon_self)
player.add_pokemon(pokemon_self_second)
battle: Battle
pokemon_op = RoundGenerator.get_instance().generate_round()

def create_battle():
    """ create a battle with the player pokemon and a random pokemon"""
    global battle
    battle = Battle(player.get_current_pokemon(), pokemon_op)
    return battle


def game_perform_attack(attack: int):
    """ perform the attack of the player and return the pokemon new stats"""
    [only_one_attack, player_attacked_first] = battle.battle_turn(
        battle.player_pokemon.get_moves()[attack],
        battle.opponent_pokemon.get_moves()[0]) # TODO : select specific attack

    return jsonify([only_one_attack, player_attacked_first, battle.player_pokemon.to_dict(), battle.opponent_pokemon.to_dict()])

def game_perform_change(position: int):
    """ change the pokemon of the player and return the pokemon new stats"""
    # get player in database
    print(position)
    player.set_current_pokemon(int(position) - 1)
    battle.player_pokemon = player.get_current_pokemon()
    battle.battle_turn(None, battle.opponent_pokemon.get_moves()[0]) # TODO : select specific attack
    return [battle.player_pokemon.to_dict(), battle.opponent_pokemon.to_dict()]

def forfet():
    """ forfet the game and return to the menu"""
    battle.handle_end_combat(False)

def battle_log_get():
    """Return the last battle log"""
    return battle.get_battle_log()