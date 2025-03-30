from models.Pokemon import Pokemon
from models.factory.MoveFactory import MoveFactory
from models.level.Stats import Stat
from models.level.XpDifficulty import XPDifficulty
from models.pokemonType.utils.PokemonTypeEnum import PokemonType

"""
Price note:
first stage price 8
second stage price 16
third stage price 30
pseudo-legendary price 50
legendary price 60
with some exception if pokemon powerfull or not
"""


class PokemonFactory:
    """
    Factory to create the most common pokemon useful also for test
    """

    @staticmethod
    def create_pikachu():
        stat = Stat(35, 55, 50, 40, 50, 90, 330, 250, 220, 120, 180, 250)
        return (
            Pokemon.Builder()
            .set_name("Pikachu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.ELECTRIC)
            .set_moves(MoveFactory.get_move("Éclair"))
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Queue de Fer"))
            .build()
        )

    @staticmethod
    def create_dracaufeu():
        stat = Stat(78, 84, 109, 78, 85, 100, 328, 280, 325, 250, 290, 315)
        return (
            Pokemon.Builder()
            .set_name("Dracaufeu")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(40)
            .set_type(PokemonType.FIRE)
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Mèche Enflammée"))
            .set_moves(MoveFactory.get_move("Griffe Dragon"))
            .build()
        )

    @staticmethod
    def create_leviator():
        stat = Stat(95, 75, 60, 79, 100, 81, 350, 270, 260, 210, 250, 270)
        return (
            Pokemon.Builder()
            .set_name("Leviator")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/130.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(60)
            .set_type(PokemonType.WATER)
            .set_type(PokemonType.FLYING)
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .build()
        )

    @staticmethod
    def create_ronflex():
        stat = Stat(160, 110, 65, 65, 110, 30, 450, 260, 310, 200, 280, 320)
        return (
            Pokemon.Builder()
            .set_name("Ronflex")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(55)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Coup de Boule"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Tacle"))
            .build()
        )

    @staticmethod
    def create_salameche():
        stat = Stat(39, 52, 43, 60, 50, 65, 270, 220, 180, 130, 170, 210)
        return (
            Pokemon.Builder()
            .set_name("Salamèche")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.FIRE)
            .set_moves(MoveFactory.get_move("Flammèche"))
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Griffe Dragon"))
            .build()
        )

    @staticmethod
    def create_carapuce():
        stat = Stat(44, 48, 65, 50, 64, 43, 280, 240, 200, 150, 190, 230)
        return (
            Pokemon.Builder()
            .set_name("Carapuce")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.WATER)
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Laser Glace"))
            .build()
        )

    @staticmethod
    def create_bulbizarre():
        stat = Stat(45, 49, 49, 65, 65, 45, 275, 230, 190, 140, 180, 220)
        return (
            Pokemon.Builder()
            .set_name("Bulbizarre")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.GRASS)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Tranch'Herbe"))
            .set_moves(MoveFactory.get_move("Bomb Beurk"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .build()
        )

    @staticmethod
    def create_ectoplasma():
        stat = Stat(60, 65, 130, 60, 75, 110, 320, 270, 310, 220, 260, 290)
        return (
            Pokemon.Builder()
            .set_name("Ectoplasma")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(60)
            .set_type(PokemonType.GHOST)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .set_moves(MoveFactory.get_move("Hypnose"))
            .set_moves(MoveFactory.get_move("Psyko"))
            .build()
        )

    @staticmethod
    def create_mewtwo():
        stat = Stat(106, 110, 154, 90, 90, 130, 385, 340, 420, 280, 340, 370)
        return (
            Pokemon.Builder()
            .set_name("Mewtwo")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(100)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Laser Glace"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .build()
        )

    @staticmethod
    def create_tyranocif():
        stat = Stat(100, 134, 95, 110, 100, 61, 380, 320, 350, 260, 310, 340)
        return (
            Pokemon.Builder()
            .set_name("Tyranocif")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/248.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(50)
            .set_type(PokemonType.ROCK)
            .set_type(PokemonType.DARK)
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Queue de Fer"))
            .build()
        )

    @staticmethod
    def create_gardevoir():
        stat = Stat(68, 65, 65, 125, 115, 80, 360, 280, 250, 200, 240, 270)
        return (
            Pokemon.Builder()
            .set_name("Gardevoir")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(50)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Mèche Enflammée"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .set_moves(MoveFactory.get_move("Éclair"))
            .build()
        )

    @staticmethod
    def create_metalosse():
        stat = Stat(70, 134, 130, 92, 80, 70, 400, 350, 310, 240, 290, 350)
        return (
            Pokemon.Builder()
            .set_name("Metalosse")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(50)
            .set_type(PokemonType.STEEL)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Queue de Fer"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .build()
        )

    @staticmethod
    def create_lucario():
        stat = Stat(70, 110, 70, 115, 70, 90, 405, 320, 270, 210, 240, 280)
        return (
            Pokemon.Builder()
            .set_name("Lucario")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(45)
            .set_type(PokemonType.FIGHT)
            .set_type(PokemonType.STEEL)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Poing Glace"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Requiem Sombre"))
            .build()
        )

    @staticmethod
    def create_rattatac():
        stat = Stat(30, 56, 35, 25, 35, 72, 210, 150, 120, 80, 100, 130)
        return (
            Pokemon.Builder()
            .set_name("Rattatac")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/19.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(8)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_etouraptor():
        stat = Stat(75, 95, 60, 85, 60, 100, 350, 280, 240, 210, 250, 280)
        return (
            Pokemon.Builder()
            .set_name("Étouraptor")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/398.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(16)
            .set_type(PokemonType.FLYING)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .build()
        )

    @staticmethod
    def create_arbok():
        stat = Stat(60, 85, 69, 65, 79, 80, 330, 250, 230, 180, 220, 270)
        return (
            Pokemon.Builder()
            .set_name("Arbok")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/24.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(16)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Bomb Beurk"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .build()
        )

    @staticmethod
    def create_tartard():
        stat = Stat(60, 80, 70, 100, 80, 70, 330, 250, 230, 200, 230, 270)
        return (
            Pokemon.Builder()
            .set_name("Tartard")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/62.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.WATER)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .set_moves(MoveFactory.get_move("Bomb Beurk"))
            .build()
        )

    @staticmethod
    def create_demolosse():
        stat = Stat(75, 90, 60, 65, 80, 105, 350, 250, 240, 200, 220, 270)
        return (
            Pokemon.Builder()
            .set_name("Démolosse")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/228.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.FIRE)
            .set_type(PokemonType.DARK)
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Poing Feu"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .build()
        )

    @staticmethod
    def create_blizzaroi():
        stat = Stat(80, 80, 70, 70, 70, 100, 350, 280, 240, 210, 250, 290)
        return (
            Pokemon.Builder()
            .set_name("Blizzaroi")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/460.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(35)
            .set_type(PokemonType.ICE)
            .set_moves(MoveFactory.get_move("Laser Glace"))
            .set_moves(MoveFactory.get_move("Poing Glacé"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .build()
        )

    @staticmethod
    def create_trioxhydre():
        stat = Stat(92, 125, 90, 90, 90, 98, 400, 320, 300, 260, 280, 310)
        return (
            Pokemon.Builder()
            .set_name("Trioxhydre")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/635.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(50)
            .set_type(PokemonType.DRAGON)
            .set_type(PokemonType.DARK)
            .set_moves(MoveFactory.get_move("Griffe Dragon"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Psychique"))
            .build()
        )

    @staticmethod
    def create_miradar():
        stat = Stat(70, 60, 50, 60, 70, 85, 300, 230, 210, 190, 220, 250)
        return (
            Pokemon.Builder()
            .set_name("Miradar")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/505.png"
            )
            .set_level(1, XPDifficulty.EASY)
            .set_stat(stat)
            .set_price(15)
            .set_type(PokemonType.NORMAL)
            .set_type(PokemonType.FLYING)
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Tornade"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .build()
        )

    @staticmethod
    def create_musteflott():
        stat = Stat(75, 60, 50, 50, 60, 95, 340, 260, 230, 180, 210, 270)
        return (
            Pokemon.Builder()
            .set_name("Mustéflott")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/418.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.WATER)
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Hydrocanon"))
            .set_moves(MoveFactory.get_move("Ball'Ombre"))
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .build()
        )

    @staticmethod
    def create_machoke():
        stat = Stat(80, 100, 70, 85, 70, 55, 350, 290, 240, 210, 230, 270)
        return (
            Pokemon.Builder()
            .set_name("Machopeur")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/67.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(22)
            .set_type(PokemonType.FIGHT)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_blastoise():
        stat = Stat(79, 83, 100, 85, 105, 78, 350, 310, 330, 250, 300, 340)
        return (
            Pokemon.Builder()
            .set_name("Tortank")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(40)
            .set_type(PokemonType.WATER)
            .set_moves(MoveFactory.get_move("Hydrocanon"))
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Laser Glace"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .build()
        )

    @staticmethod
    def create_golem():
        stat = Stat(80, 120, 130, 55, 65, 45, 340, 310, 380, 270, 310, 340)
        return (
            Pokemon.Builder()
            .set_name("Golem")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/76.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(45)
            .set_type(PokemonType.GROUND)
            .set_type(PokemonType.ROCK)
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_ponyta():
        stat = Stat(50, 85, 55, 65, 65, 90, 300, 250, 220, 180, 210, 240)
        return (
            Pokemon.Builder()
            .set_name("Ponita")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/77.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.FIRE)
            .set_moves(MoveFactory.get_move("Flammèche"))
            .set_moves(MoveFactory.get_move("Mèche Enflammée"))
            .set_moves(MoveFactory.get_move("Coup de Boule"))
            .build()
        )

    @staticmethod
    def create_farfetchd():
        stat = Stat(52, 65, 55, 58, 50, 60, 310, 260, 230, 190, 220, 240)
        return (
            Pokemon.Builder()
            .set_name("Canarticho")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/83.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.NORMAL)
            .set_type(PokemonType.FLYING)
            .set_moves(MoveFactory.get_move("Rafale Piquante"))
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Tornade"))
            .build()
        )

    @staticmethod
    def create_tangela():
        stat = Stat(65, 55, 115, 60, 40, 60, 290, 270, 240, 220, 240, 280)
        return (
            Pokemon.Builder()
            .set_name("Tangela")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/114.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.GRASS)
            .set_moves(MoveFactory.get_move("Toxik"))
            .set_moves(MoveFactory.get_move("Tranch'Herbe"))
            .set_moves(MoveFactory.get_move("Coup de Boule"))
            .set_moves(MoveFactory.get_move("Bomb Beurk"))
            .build()
        )

    @staticmethod
    def create_exeggutor():
        stat = Stat(95, 125, 85, 110, 75, 45, 400, 350, 300, 230, 270, 300)
        return (
            Pokemon.Builder()
            .set_name("Exeggutor")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/103.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(45)
            .set_type(PokemonType.GRASS)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Tranch'Herbe"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .set_moves(MoveFactory.get_move("Poing Glace"))
            .build()
        )

    @staticmethod
    def create_machop():
        stat = Stat(70, 80, 50, 35, 35, 35, 280, 220, 180, 140, 160, 200)
        return (
            Pokemon.Builder()
            .set_name("Machoc")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/66.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(12)
            .set_type(PokemonType.FIGHT)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_onix():
        stat = Stat(35, 45, 160, 30, 45, 70, 280, 240, 220, 170, 180, 200)
        return (
            Pokemon.Builder()
            .set_name("Onix")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/95.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.ROCK)
            .set_type(PokemonType.GROUND)
            .set_moves(MoveFactory.get_move("Tacle"))
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_sandslash():
        stat = Stat(75, 100, 110, 55, 65, 65, 350, 300, 270, 230, 260, 310)
        return (
            Pokemon.Builder()
            .set_name("Sabelette")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/28.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.GROUND)
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_persian():
        stat = Stat(65, 60, 60, 65, 50, 115, 300, 250, 240, 200, 210, 270)
        return (
            Pokemon.Builder()
            .set_name("Persian")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/53.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(22)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_mackogneur():
        stat = Stat(90, 130, 80, 65, 85, 55, 450, 350, 300, 280, 230, 290)
        return (
            Pokemon.Builder()
            .set_name("Mackogneur")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/68.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(40)
            .set_type(PokemonType.FIGHT)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_triopikeur():
        stat = Stat(35, 100, 50, 50, 50, 120, 300, 270, 250, 200, 210, 250)
        return (
            Pokemon.Builder()
            .set_name("Triopikeur")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/51.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.GROUND)
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Coup de Roc"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_ferosinge():
        stat = Stat(40, 80, 35, 35, 45, 70, 300, 250, 220, 190, 210, 230)
        return (
            Pokemon.Builder()
            .set_name("Férosinge")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/56.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(15)
            .set_type(PokemonType.FIGHT)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_kangourex():
        stat = Stat(105, 95, 80, 40, 70, 90, 370, 330, 310, 250, 280, 320)
        return (
            Pokemon.Builder()
            .set_name("Kangourex")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/115.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(50)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .build()
        )

    @staticmethod
    def create_sablenite():
        stat = Stat(50, 70, 90, 60, 50, 70, 280, 260, 230, 210, 220, 240)
        return (
            Pokemon.Builder()
            .set_name("Sablenite")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/504.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(25)
            .set_type(PokemonType.GROUND)
            .set_moves(MoveFactory.get_move("Séisme"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_seviper():
        stat = Stat(73, 100, 60, 60, 60, 65, 340, 300, 270, 230, 240, 270)
        return (
            Pokemon.Builder()
            .set_name("Seviper")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/336.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(30)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_lunatone():
        stat = Stat(70, 55, 65, 95, 85, 70, 350, 320, 300, 260, 280, 310)
        return (
            Pokemon.Builder()
            .set_name("Lunatone")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/337.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(35)
            .set_type(PokemonType.ROCK)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Poing Glace"))
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_solrock():
        stat = Stat(70, 95, 85, 55, 65, 70, 350, 320, 310, 260, 280, 300)
        return (
            Pokemon.Builder()
            .set_name("Solrock")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/338.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(35)
            .set_type(PokemonType.ROCK)
            .set_type(PokemonType.PSYCHIC)
            .set_moves(MoveFactory.get_move("Poing Glace"))
            .set_moves(MoveFactory.get_move("Psychique"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_cradopaud():
        stat = Stat(60, 70, 55, 40, 50, 55, 280, 240, 220, 190, 200, 230)
        return (
            Pokemon.Builder()
            .set_name("Cradopaud")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/453.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.POISON)
            .set_moves(MoveFactory.get_move("Poing de Fer"))
            .set_moves(MoveFactory.get_move("Mâchouille"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .build()
        )

    @staticmethod
    def create_brasegali():
        stat = Stat(80, 120, 70, 85, 60, 90, 350, 300, 280, 230, 250, 300)
        return (
            Pokemon.Builder()
            .set_name("Braségali")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(45)
            .set_type(PokemonType.FIRE)
            .set_type(PokemonType.FIGHT)
            .set_moves(MoveFactory.get_move("Flammèche"))
            .set_moves(MoveFactory.get_move("Poing Feu"))
            .set_moves(MoveFactory.get_move("Coup de Pied"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .build()
        )

    @staticmethod
    def create_aquali():
        stat = Stat(65, 60, 50, 44, 50, 55, 280, 240, 210, 190, 210, 240)
        return (
            Pokemon.Builder()
            .set_name("Aquali")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/134.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(30)
            .set_type(PokemonType.WATER)
            .set_moves(MoveFactory.get_move("Hydrocanon"))
            .set_moves(MoveFactory.get_move("Surf"))
            .set_moves(MoveFactory.get_move("Laser Glace"))
            .build()
        )

    @staticmethod
    def create_herbizarre():
        stat = Stat(60, 49, 49, 65, 65, 45, 280, 230, 190, 180, 200, 220)
        return (
            Pokemon.Builder()
            .set_name("Herbizarre")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/2.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(20)
            .set_type(PokemonType.GRASS)
            .set_moves(MoveFactory.get_move("Tranch'Herbe"))
            .set_moves(MoveFactory.get_move("Morsure"))
            .set_moves(MoveFactory.get_move("Coup de Boule"))
            .build()
        )

    @staticmethod
    def create_chrysacier():
        stat = Stat(45, 30, 35, 20, 20, 45, 140, 110, 90, 70, 90, 110)
        return (
            Pokemon.Builder()
            .set_name("Chrysacier")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/11.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(7)
            .set_type(PokemonType.BUG)
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Coup de Boule"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .build()
        )

    @staticmethod
    def create_evoli():
        stat = Stat(55, 55, 50, 45, 50, 55, 320, 270, 230, 190, 230, 250)
        return (
            Pokemon.Builder()
            .set_name("Évoli")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
            )
            .set_level(1, XPDifficulty.NORMAL)
            .set_stat(stat)
            .set_price(15)
            .set_type(PokemonType.NORMAL)
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Toxik"))
            .set_moves(MoveFactory.get_move("Morsure"))
            .build()
        )

    @staticmethod
    def create_voltali():
        stat = Stat(65, 65, 60, 110, 95, 65, 370, 320, 280, 240, 270, 310)
        return (
            Pokemon.Builder()
            .set_name("Voltali")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/135.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(40)
            .set_type(PokemonType.ELECTRIC)
            .set_moves(MoveFactory.get_move("Éclair"))
            .set_moves(MoveFactory.get_move("Tonnerre"))
            .set_moves(MoveFactory.get_move("Paralysie"))
            .set_moves(MoveFactory.get_move("Morsure"))
            .build()
        )

    @staticmethod
    def create_pyroli():
        stat = Stat(65, 65, 60, 100, 85, 65, 370, 320, 290, 240, 270, 310)
        return (
            Pokemon.Builder()
            .set_name("Pyroli")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/136.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(35)
            .set_type(PokemonType.FIRE)
            .set_moves(MoveFactory.get_move("Flammèche"))
            .set_moves(MoveFactory.get_move("Lance-Flamme"))
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Morsure"))
            .build()
        )

    @staticmethod
    def create_noctali():
        stat = Stat(65, 60, 70, 60, 130, 60, 370, 330, 290, 250, 290, 330)
        return (
            Pokemon.Builder()
            .set_name("Noctali")
            .set_img(
                "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/197.png"
            )
            .set_level(1, XPDifficulty.HARD)
            .set_stat(stat)
            .set_price(40)
            .set_type(PokemonType.DARK)
            .set_moves(MoveFactory.get_move("Griffe"))
            .set_moves(MoveFactory.get_move("Morsure"))
            .set_moves(MoveFactory.get_move("Paralysie"))
            .build()
        )

    @staticmethod
    def get_all_staticmethod():
        # get all static methods
        return [
            getattr(PokemonFactory, func)
            for func in dir(PokemonFactory)
            if callable(getattr(PokemonFactory, func)) and func.startswith("create_")
        ]

    @staticmethod
    def get_shop_pokemons():
        methods_create = PokemonFactory.get_all_staticmethod()
        pokemons = []
        for method in methods_create:
            pokemons.append(method())

        pokemons.sort(key=lambda x: x.price)
        return pokemons
