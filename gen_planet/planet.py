import random

from gen_planet import moon
from gen_planet.entity import Entity


class Planet(Entity):
    def __init__(self, parent, num_children=None):
        super().__init__(parent, num_children=num_children)
        self.gen_moons(random.randint(0, 6))

    def display(self):
        print(f'{"":{self.left_padding}}{self.OUTLINE}')
        super().display()
        self.moons.display()
        print(f'{"":{self.left_padding}}{self.OUTLINE}')

    def gen_moons(self, num_moons):
        self.moons = moon.MoonSet(self, num_children=num_moons)
