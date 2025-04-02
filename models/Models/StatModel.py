from models.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class StatModel(db.Model):
    __tablename__ = "stat"
    id = db.Column(db.Integer, primary_key=True)
    base_hp = db.Column(db.Integer)
    base_attack = db.Column(db.Integer)
    base_attack_special = db.Column(db.Integer)
    base_defense = db.Column(db.Integer)
    base_defense_special = db.Column(db.Integer)
    base_speed = db.Column(db.Integer)
    max_hp = db.Column(db.Integer)
    max_attack = db.Column(db.Integer)
    max_attack_special = db.Column(db.Integer)
    max_defense = db.Column(db.Integer)
    max_defense_special = db.Column(db.Integer)
    max_speed = db.Column(db.Integer)
    current_hp = db.Column(db.Integer)

    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemon.id"), nullable=False)
    pokemon = db.relationship("PokemonModel", back_populates="stat")
