class Player:
    def __init__(self):
        self.money = 0
        self._pokemon = [None] * 6
        self.record_round = 0

    @property.setter
    def pokemon(self, value):
