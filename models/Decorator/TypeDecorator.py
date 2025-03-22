from models.Decorator.Component import Component


class TypeDecorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def get_types(self):
        return self._component.get_types()

    def get_resistances(self):
        return self._component.get_resistances()

    def get_weaknesses(self):
        return self._component.get_weaknesses()
