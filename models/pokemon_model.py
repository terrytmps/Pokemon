from models.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PokemonModel(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    position = db.Column(db.Integer)

    def __repr__(self):
        return f"<Pokemon {self.name}>"
