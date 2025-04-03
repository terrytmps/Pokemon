from models.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PlayerModel(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    money = db.Column(db.Integer, default=0)
    record_round = db.Column(db.Integer, default=0)
    current_pokemon_index = db.Column(db.Integer, default=0)

    pokemons = db.relationship(
        "PokemonModel",
        backref="player",
        lazy=True,
        foreign_keys="PokemonModel.player_id",
        cascade="all, delete-orphan",
    )
