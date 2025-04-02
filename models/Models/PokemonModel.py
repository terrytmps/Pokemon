from models.Database import DatabaseSingleton
from models.Models.PlayerModel import pokemon_moves_table
from models.status.StatusEnum import StatusEnum

db = DatabaseSingleton.get_instance().get_db()


class PokemonModel(db.Model):
    __tablename__ = "pokemon"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sprite_url = db.Column(db.String(255))
    price = db.Column(db.Integer, nullable=False)
    current_status = db.Column(db.Enum(StatusEnum), default=StatusEnum.NORMAL)

    player_id = db.Column(
        db.Integer,
        db.ForeignKey("player.id", use_alter=True, name="fk_pokemon_player"),
        nullable=True,
    )

    level = db.Column(db.Integer, nullable=False)

    stat = db.relationship(
        "StatModel",
        uselist=False,
        back_populates="pokemon",
        cascade="all, delete-orphan",
    )

    moves = db.relationship(
        "MoveModel",
        secondary=pokemon_moves_table,
        lazy="subquery",
        backref=db.backref("pokemons", lazy=True),
    )
