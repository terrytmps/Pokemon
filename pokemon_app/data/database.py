from flask_sqlalchemy import SQLAlchemy


class DatabaseSingleton:
    _instance = None
    _db = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            if app is not None:
                cls._db = SQLAlchemy(app)
        return cls._instance

    @classmethod
    def get_instance(cls, app=None):
        if cls._instance is None:
            cls._instance = DatabaseSingleton(app)
        return cls._instance

    def get_db(self):
        if self._db is None:
            raise ValueError(
                "Database not initialized. Provide an app when creating the first instance."
            )
        return self._db
