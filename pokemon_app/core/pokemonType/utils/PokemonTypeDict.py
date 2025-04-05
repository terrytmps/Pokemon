"""
Dictionary of all Pokemon types into the decorator pattern
"""

from models.pokemonType.BugTypeDecorator import BugTypeDecorator
from models.pokemonType.DarkTypeDecorator import DarkTypeDecorator
from models.pokemonType.DragonTypeDecorator import DragonTypeDecorator
from models.pokemonType.ElectricTypeDecorator import ElectricTypeDecorator
from models.pokemonType.FightingTypeDecorator import FightingTypeDecorator
from models.pokemonType.FireTypeDecorator import FireTypeDecorator
from models.pokemonType.FlyingTypeDecorator import FlyingTypeDecorator
from models.pokemonType.GhostTypeDecorator import GhostTypeDecorator
from pokemon_app.core.pokemonType.GrassTypeDecorator import GrassTypeDecorator
from models.pokemonType.GroundTypeDecorator import GroundTypeDecorator
from models.pokemonType.IceTypeDecorator import IceTypeDecorator
from models.pokemonType.NormalTypeDecorator import NormalTypeDecorator
from models.pokemonType.PoisonTypeDecorator import PoisonTypeDecorator
from models.pokemonType.PsychicTypeDecorator import PsychicTypeDecorator
from models.pokemonType.RockTypeDecorator import RockTypeDecorator
from models.pokemonType.SteelTypeDecorator import SteelTypeDecorator
from models.pokemonType.WaterTypeDecorator import WaterTypeDecorator
from models.pokemonType.utils.PokemonTypeEnum import PokemonType

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
