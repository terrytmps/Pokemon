from models.Database import DatabaseSingleton
from models.Pokemon import Pokemon
from models.status.StatusEnum import StatusEnum
from sqlalchemy import Column, Integer, String, Enum

# Obtenir l'instance de la base de données
db = DatabaseSingleton.get_instance().get_db()

# Définir les modèles SQLAlchemy
class DBPokemon(db.Model):
    __tablename__ = 'pokemons'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    sprite_url = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.NORMAL)

class PokemonDBAdapter:
    """
    Adaptateur pour convertir les objets Pokemon vers/depuis la base de données
    """
    
    @staticmethod
    def to_db_model(pokemon):
        """
        Convertit un objet Pokemon en modèles de base de données
        """
        
        # Créer l'objet Pokemon DB
        db_pokemon = DBPokemon(
            name=pokemon.name,
            sprite_url=pokemon.sprite_url,
            price=pokemon.price,
            status=pokemon.status,
        )
        
        return db_pokemon
    
    @staticmethod
    def from_db_model(db_pokemon):
        """
        Convertit les modèles de base de données en objet Pokemon
        """
        
        # Utiliser le builder Pokemon
        builder = Pokemon.Builder()
        builder.set_name(db_pokemon.name)
        builder.set_img(db_pokemon.sprite_url)
        builder.set_price(db_pokemon.price)
        builder.set_level(db_pokemon.level.level, db_pokemon.level.xp_difficulty)
        
        # Ajouter les types
        if db_pokemon.first_type:
            builder.set_type(db_pokemon.first_type)
        if db_pokemon.second_type:
            builder.set_type(db_pokemon.second_type)
        
        # Créer le Pokémon
        pokemon = builder.build()
        
        # Définir status et HP courant
        pokemon.set_status(db_pokemon.status)
        pokemon.stat.current_hp = db_pokemon.stat.current_hp
        
        # Ajouter les moves
        for db_move in db_pokemon.moves:
            # Vous devrez créer un Move à partir de db_move selon votre implémentation
            move = create_move_from_db(db_move)
            pokemon.addMove(move)
        
        return pokemon

def create_move_from_db(db_move):
    """
    Fonction auxiliaire pour créer un Move à partir d'un DBMove
    Cette implémentation dépendra de votre classe Move
    """
    # Remplacez ceci par votre implémentation réelle de Move
    from models.Move import Move  # Importez votre classe Move
    
    # Adaptez cette partie selon la structure de votre classe Move
    move = Move(db_move.name)
    if hasattr(db_move, 'power') and db_move.power is not None:
        move.power = db_move.power
    if hasattr(db_move, 'accuracy') and db_move.accuracy is not None:
        move.accuracy = db_move.accuracy
        
    return move

# Exemple d'utilisation
def save_pokemon(pokemon):
    """
    Sauvegarde un Pokémon dans la base de données
    """
    db_pokemon = PokemonDBAdapter.to_db_model(pokemon)
    db.session.add(db_pokemon)
    db.session.commit()
    return db_pokemon.id

def load_pokemon(pokemon_id):
    """
    Charge un Pokémon depuis la base de données
    """
    db_pokemon = DBPokemon.query.get(pokemon_id)
    if db_pokemon:
        return PokemonDBAdapter.from_db_model(db_pokemon)
    return None