from pokemon_app.data.database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PokemonModel(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    player_id = db.Column(
        db.Integer,
        db.ForeignKey("player.id", use_alter=True, name="fk_pokemon_player"),
        nullable=True,
    )

    level = db.Column(db.Integer, nullable=False)
