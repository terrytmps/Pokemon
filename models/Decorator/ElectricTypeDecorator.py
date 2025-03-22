from models.Decorator.TypeDecorator import TypeDecorator


class ElectricTypeDecorator(TypeDecorator):
    def __init__(self, component):
        super().__init__(component)

    def get_types(self):
        types = self._component.get_types()
        types.append("Electric")
        return types

    def get_resistances(self):
        resistances = self._component.get_resistances()
        resistances.extend(["Electric", "Flying", "Steel"])
        return resistances

    def get_weaknesses(self):
        weaknesses = self._component.get_weaknesses()
        weaknesses.append("Ground")
        return weaknesses
