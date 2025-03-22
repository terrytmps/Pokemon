from models.Decorator.TypeDecorator import TypeDecorator


class WaterTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append("Water")
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(["Water", "Fire", "Ice", "Steel"])
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.extend(["Electric", "Grass"])
        return weaknesses
