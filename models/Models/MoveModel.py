from models.Database import DatabaseSingleton
from models.enum.MoveCategory import MoveCategory
from models.pokemonType.utils.PokemonTypeEnum import PokemonType
from models.status.StatusEnum import StatusEnum

db = DatabaseSingleton.get_instance().get_db()


class MoveModel(db.Model):
    __tablename__ = "move"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    power = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    move_type = db.Column(db.Enum(PokemonType))
    move_category = db.Column(db.Enum(MoveCategory))
    move_effect = db.Column(db.Enum(StatusEnum), default=StatusEnum.NORMAL)
