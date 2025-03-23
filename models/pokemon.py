from models.level.Level import Level
from models.level.LevelObservable import LevelObservable
from models.level.Stats import Stat
from models.status.StatusEnum import StatusEnum


class Pokemon(LevelObservable):
    """
    Classe that represent a pokemon with all its attributes and behavior
    """

    def __init__(
            self,
            name: str,
            sprite_url: str,
            price: int,
            level: Level,
            stat: Stat
    ):
        super().__init__()
        self._status = StatusEnum.NORMAL
        self.name = name
        self.__level = level
        self.__stat = stat
        self._sprite_url = sprite_url
        self._moves = [None] * 4
        self.price = price

    def max_hp(self):
        return self.__stat.current_max_hp

    def get_current_hp(self):
        return self.__stat.current_hp

    def get_current_max_hp(self):
        return self.__stat.current_max_hp

    def get_level_object(self):
        return self.__level

    @property
    def sprite_url(self):
        return self._sprite_url

    @property
    def stat(self):
        return self.__stat

    @property
    def level(self):
        return self.__level.level

    @property
    def first_type(self):
        return None

    @property
    def second_type(self):
        return None

    @property
    def status(self):
        return self._status

    def set_status(self, status: StatusEnum):
        self._status = status

    def gain_experience(self, xp: int):
        """
        Gain X amount of experience at the end of the fight
        """
        self.__level.gain_experience(xp)

    def addMove(self, move) -> bool:
        """
        Try to add a move return boolean meaning success of operation
        """
        for i in range(4):
            if self._moves[i] is None:
                self._moves[i] = move
                return True
        return False

    def replaceMove(self, move, index) -> bool:
        """
        Try to replace a move return boolean meaning success of operation
        """

        if index < 0 or index > 3:
            return False
        self._moves[index] = move
        return True

    ## Decorator pattern methods

    def get_types(self):
        """
        Return the types of the pokemon
        """
        return []

    def get_resistances(self):
        """ "
        Return the resistances of the pokemon
        """
        return []

    def get_weaknesses(self):
        """
        Return the weaknesses of the pokemon
        """
        return []

    def get_immunity(self):
        """
        Return the immunities of the pokemon
        """
        return []
