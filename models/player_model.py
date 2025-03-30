from models.Database import DatabaseSingleton

db = DatabaseSingleton.get_instance().get_db()


class PlayerModel(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True, default="Player")
    money = db.Column(db.Integer, default=0)
    record_round = db.Column(db.Integer, default=0)
    current_pokemon = db.Column(db.Integer, default=-1)

    def __repr__(self):
        return f"<Player {self.id}>"
