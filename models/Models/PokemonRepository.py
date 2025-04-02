from models.Database import DatabaseSingleton
from models.Move import Move
from models.Pokemon import Pokemon
from models.Models.PokemonModel import PokemonModel
from models.Models.StatModel import StatModel
from models.Models.MoveModel import MoveModel
from models.level.Level import Level
from models.level.Stats import Stat
from models.level.XpDifficulty import XPDifficulty

db = DatabaseSingleton.get_instance().get_db()


class PokemonRepository:
    @staticmethod
    def save(pokemon: Pokemon, player_id: int = None) -> int:
        """
        Save a Pokémon in the database
        """
        pokemon_id = getattr(pokemon, "id", None)
        pokemon_model = None

        if pokemon_id:
            pokemon_model = PokemonModel.query.get(pokemon_id)

        if pokemon_model is None:
            pokemon_model = PokemonModel(
                name=pokemon.name,
                sprite_url=pokemon.sprite_url,
                price=pokemon.price,
                current_status=pokemon.status_strategy.get_status(),
                player_id=player_id,
                level=pokemon.level,
            )
            db.session.add(pokemon_model)
        else:
            pokemon_model.name = pokemon.name
            pokemon_model.sprite_url = pokemon.sprite_url
            pokemon_model.price = pokemon.price
            pokemon_model.current_status = pokemon.status_strategy.get_status()
            pokemon_model.player_id = player_id

        if hasattr(pokemon, "stat") and pokemon.stat:
            if pokemon_model.stat:
                pokemon_model.stat.base_hp = pokemon.stat.base_hp
                pokemon_model.stat.base_attack = pokemon.stat.base_attack
                pokemon_model.stat.base_attack_special = (
                    pokemon.stat.base_attack_special
                )
                pokemon_model.stat.base_defense = pokemon.stat.base_defense
                pokemon_model.stat.base_defense_special = (
                    pokemon.stat.base_defense_special
                )
                pokemon_model.stat.base_speed = pokemon.stat.base_speed
                pokemon_model.stat.max_hp = pokemon.stat.max_hp
                pokemon_model.stat.max_attack = pokemon.stat.max_attack
                pokemon_model.stat.max_attack_special = pokemon.stat.max_attack_special
                pokemon_model.stat.max_defense = pokemon.stat.max_defense
                pokemon_model.stat.max_defense_special = (
                    pokemon.stat.max_defense_special
                )
                pokemon_model.stat.max_speed = pokemon.stat.max_speed
                pokemon_model.stat.current_hp = pokemon.stat.current_hp
            else:
                stat_model = StatModel(
                    base_hp=pokemon.stat.base_hp,
                    base_attack=pokemon.stat.base_attack,
                    base_attack_special=pokemon.stat.base_attack_special,
                    base_defense=pokemon.stat.base_defense,
                    base_defense_special=pokemon.stat.base_defense_special,
                    base_speed=pokemon.stat.base_speed,
                    max_hp=pokemon.stat.max_hp,
                    max_attack=pokemon.stat.max_attack,
                    max_attack_special=pokemon.stat.max_attack_special,
                    max_defense=pokemon.stat.max_defense,
                    max_defense_special=pokemon.stat.max_defense_special,
                    max_speed=pokemon.stat.max_speed,
                    current_hp=pokemon.stat.current_hp,
                )
                pokemon_model.stat = stat_model

        if hasattr(pokemon, "_moves"):
            pokemon_model.moves = []

            for move in pokemon.get_moves():
                if move is not None:
                    move_model = MoveModel.query.filter_by(name=move.name).first()
                    if not move_model:
                        move_model = MoveModel(
                            name=move.name,
                            description=move.description,
                            power=move.power,
                            accuracy=move.accuracy,
                            move_type=move.move_type,
                            move_category=move.move_category,
                            move_effect=move.move_effect,
                        )
                        db.session.add(move_model)

                    pokemon_model.moves.append(move_model)

        db.session.commit()

        if not hasattr(pokemon, "id"):
            pokemon.id = pokemon_model.id

        return pokemon_model.id

    @staticmethod
    def find_by_id(pokemon_id: int) -> Pokemon | None:
        """
        Load a pokemon from the database
        """
        pokemon_model = PokemonModel.query.get(pokemon_id)
        if not pokemon_model:
            return None

        if pokemon_model.level:
            level = Level(pokemon_model.level, XPDifficulty.EASY)
        else:
            level = None

        if pokemon_model.stat:
            stat = Stat(
                base_hp=pokemon_model.stat.base_hp,
                base_attack=pokemon_model.stat.base_attack,
                base_attack_special=pokemon_model.stat.base_attack_special,
                base_defense=pokemon_model.stat.base_defense,
                base_defense_special=pokemon_model.stat.base_defense_special,
                base_speed=pokemon_model.stat.base_speed,
                max_hp=pokemon_model.stat.max_hp,
                max_attack=pokemon_model.stat.max_attack,
                max_attack_special=pokemon_model.stat.max_attack_special,
                max_defense=pokemon_model.stat.max_defense,
                max_defense_special=pokemon_model.stat.max_defense_special,
                max_speed=pokemon_model.stat.max_speed,
            )
        else:
            stat = None

        pokemon = Pokemon(
            name=pokemon_model.name,
            sprite_url=pokemon_model.sprite_url,
            price=pokemon_model.price,
            level=level,
            stat=stat,
        )

        pokemon.id = pokemon_model.id

        for i, move_model in enumerate(pokemon_model.moves):
            if i < 4:
                move = Move(
                    move_model.name,
                    move_model.description,
                    move_model.power,
                    move_model.accuracy,
                    move_model.move_type,
                    move_model.move_category,
                    move_model.move_effect,
                )
                pokemon.get_moves()[i] = move

        return pokemon
