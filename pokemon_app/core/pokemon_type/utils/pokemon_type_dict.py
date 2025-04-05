"""
Dictionary of all Pokemon types into the decorator pattern
"""

from pokemon_app.core.pokemon_type.bug_type_decorator import BugTypeDecorator
from pokemon_app.core.pokemon_type.dark_type_decorator import DarkTypeDecorator
from pokemon_app.core.pokemon_type.dragon_type_decorator import DragonTypeDecorator
from pokemon_app.core.pokemon_type.electric_type_decorator import ElectricTypeDecorator
from pokemon_app.core.pokemon_type.fighting_type_decorator import FightingTypeDecorator
from pokemon_app.core.pokemon_type.fire_type_decorator import FireTypeDecorator
from pokemon_app.core.pokemon_type.flying_type_decorator import FlyingTypeDecorator
from pokemon_app.core.pokemon_type.ghost_type_decorator import GhostTypeDecorator
from pokemon_app.core.pokemon_type.grass_type_decorator import GrassTypeDecorator
from pokemon_app.core.pokemon_type.ground_type_decorator import GroundTypeDecorator
from pokemon_app.core.pokemon_type.ice_type_decorator import IceTypeDecorator
from pokemon_app.core.pokemon_type.normal_type_decorator import NormalTypeDecorator
from pokemon_app.core.pokemon_type.poison_type_decorator import PoisonTypeDecorator
from pokemon_app.core.pokemon_type.psychic_type_decorator import PsychicTypeDecorator
from pokemon_app.core.pokemon_type.rock_type_decorator import RockTypeDecorator
from pokemon_app.core.pokemon_type.steel_type_decorator import SteelTypeDecorator
from pokemon_app.core.pokemon_type.water_type_decorator import WaterTypeDecorator
from pokemon_app.core.pokemon_type.utils.pokemon_type_enum import PokemonType

dict_from_enum_to_decorator = {
    PokemonType.BUG: BugTypeDecorator,
    PokemonType.DARK: DarkTypeDecorator,
    PokemonType.DRAGON: DragonTypeDecorator,
    PokemonType.ELECTRIC: ElectricTypeDecorator,
    PokemonType.FIGHT: FightingTypeDecorator,
    PokemonType.FIRE: FireTypeDecorator,
    PokemonType.FLYING: FlyingTypeDecorator,
    PokemonType.GHOST: GhostTypeDecorator,
    PokemonType.GRASS: GrassTypeDecorator,
    PokemonType.GROUND: GroundTypeDecorator,
    PokemonType.ICE: IceTypeDecorator,
    PokemonType.NORMAL: NormalTypeDecorator,
    PokemonType.POISON: PoisonTypeDecorator,
    PokemonType.PSYCHIC: PsychicTypeDecorator,
    PokemonType.ROCK: RockTypeDecorator,
    PokemonType.STEEL: SteelTypeDecorator,
    PokemonType.WATER: WaterTypeDecorator,
}
