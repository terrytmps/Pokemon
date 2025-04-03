from enum import Enum

from models.factory.PokemonFactory import PokemonFactory


# Define an Enum for Pokémon names
class PokemonName(Enum):
    PIKACHU = "Pikachu"
    DRACAUFEU = "Dracaufeu"
    LEVIATOR = "Leviator"
    RONFLEX = "Ronflex"
    SALAMECHE = "Salamèche"
    CARAPUCE = "Carapuce"
    BULBIZARRE = "Bulbizarre"
    ECTOPLASMA = "Ectoplasma"
    MEWTWO = "Mewtwo"
    TYRANOCIF = "Tyranocif"
    GARDEVOIR = "Gardevoir"
    METALOSSE = "Metalosse"
    LUCARIO = "Lucario"
    RATTATAC = "Rattatac"
    ETOURAPTOR = "Étouraptor"
    ARBOK = "Arbok"
    TARTARD = "Tartard"
    DEMOLOSSE = "Démolosse"
    BLIZZAROI = "Blizzaroi"
    TRIOXHYDRE = "Trioxhydre"
    MIRADAR = "Miradar"
    MUSTEFLOTT = "Mustéflott"
    MACHOP = "Machopeur"
    BLASTOISE = "Tortank"
    GOLEM = "Golem"
    PONYTA = "Ponita"
    FARFETCHD = "Canarticho"
    TANGELA = "Tangela"
    EXEGGUTOR = "Exeggutor"
    ONIX = "Onix"
    SANDSLASH = "Sabelette"
    PERSIAN = "Persian"
    MACKOGNEUR = "Mackogneur"
    TRIOPIKEUR = "Triopikeur"
    FEROSINGE = "Férosinge"
    KANGOUREX = "Kangourex"
    SABLENITE = "Sablenite"
    SEVIPER = "Seviper"
    LUNATONE = "Lunatone"
    SOLROCK = "Solrock"
    CRADOPAUD = "Cradopaud"
    BRASEGALI = "Braségali"
    AQUALI = "Aquali"
    HERBIZARRE = "Herbizarre"
    CHRYSACIER = "Chrysacier"
    EVOLI = "Évoli"
    VOLTALI = "Voltali"
    PYROLI = "Pyroli"
    NOCTALI = "Noctali"


# Map Pokémon names to their creation methods
pokemon_factory_methods = {
    PokemonName.PIKACHU: PokemonFactory.create_pikachu,
    PokemonName.DRACAUFEU: PokemonFactory.create_dracaufeu,
    PokemonName.LEVIATOR: PokemonFactory.create_leviator,
    PokemonName.RONFLEX: PokemonFactory.create_ronflex,
    PokemonName.SALAMECHE: PokemonFactory.create_salameche,
    PokemonName.CARAPUCE: PokemonFactory.create_carapuce,
    PokemonName.BULBIZARRE: PokemonFactory.create_bulbizarre,
    PokemonName.ECTOPLASMA: PokemonFactory.create_ectoplasma,
    PokemonName.MEWTWO: PokemonFactory.create_mewtwo,
    PokemonName.TYRANOCIF: PokemonFactory.create_tyranocif,
    PokemonName.GARDEVOIR: PokemonFactory.create_gardevoir,
    PokemonName.METALOSSE: PokemonFactory.create_metalosse,
    PokemonName.LUCARIO: PokemonFactory.create_lucario,
    PokemonName.RATTATAC: PokemonFactory.create_rattatac,
    PokemonName.ETOURAPTOR: PokemonFactory.create_etouraptor,
    PokemonName.ARBOK: PokemonFactory.create_arbok,
    PokemonName.TARTARD: PokemonFactory.create_tartard,
    PokemonName.DEMOLOSSE: PokemonFactory.create_demolosse,
    PokemonName.BLIZZAROI: PokemonFactory.create_blizzaroi,
    PokemonName.TRIOXHYDRE: PokemonFactory.create_trioxhydre,
    PokemonName.MIRADAR: PokemonFactory.create_miradar,
    PokemonName.MUSTEFLOTT: PokemonFactory.create_musteflott,
    PokemonName.MACHOP: PokemonFactory.create_machoke,
    PokemonName.BLASTOISE: PokemonFactory.create_blastoise,
    PokemonName.GOLEM: PokemonFactory.create_golem,
    PokemonName.PONYTA: PokemonFactory.create_ponyta,
    PokemonName.FARFETCHD: PokemonFactory.create_farfetchd,
    PokemonName.TANGELA: PokemonFactory.create_tangela,
    PokemonName.EXEGGUTOR: PokemonFactory.create_exeggutor,
    PokemonName.ONIX: PokemonFactory.create_onix,
    PokemonName.SANDSLASH: PokemonFactory.create_sandslash,
    PokemonName.PERSIAN: PokemonFactory.create_persian,
    PokemonName.MACKOGNEUR: PokemonFactory.create_mackogneur,
    PokemonName.TRIOPIKEUR: PokemonFactory.create_triopikeur,
    PokemonName.FEROSINGE: PokemonFactory.create_ferosinge,
    PokemonName.KANGOUREX: PokemonFactory.create_kangourex,
    PokemonName.SABLENITE: PokemonFactory.create_sablenite,
    PokemonName.SEVIPER: PokemonFactory.create_seviper,
    PokemonName.LUNATONE: PokemonFactory.create_lunatone,
    PokemonName.SOLROCK: PokemonFactory.create_solrock,
    PokemonName.CRADOPAUD: PokemonFactory.create_cradopaud,
    PokemonName.BRASEGALI: PokemonFactory.create_brasegali,
    PokemonName.AQUALI: PokemonFactory.create_aquali,
    PokemonName.HERBIZARRE: PokemonFactory.create_herbizarre,
    PokemonName.CHRYSACIER: PokemonFactory.create_chrysacier,
    PokemonName.EVOLI: PokemonFactory.create_evoli,
    PokemonName.VOLTALI: PokemonFactory.create_voltali,
    PokemonName.PYROLI: PokemonFactory.create_pyroli,
    PokemonName.NOCTALI: PokemonFactory.create_noctali,
}


def get_enum_by_value(value: str) -> PokemonName | None:
    for name in PokemonName:
        if name.value == value:
            return name
    return None


def create_pokemon(pokemon_name: PokemonName):
    if pokemon_name in pokemon_factory_methods:
        return pokemon_factory_methods[pokemon_name]()
    else:
        raise ValueError(f"No factory method found for {pokemon_name}")
