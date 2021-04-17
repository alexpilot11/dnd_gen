import random

from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import enums, moon
from gen_planet.entity import Entity


class Planet(Entity):
    def __init__(self):
        super().__init__()
        self.gen_moons()

    def display(self):
        print(self.OUTLINE)
        super().display()
        self.moons.display()
        print(self.OUTLINE)

    def gen_moons(self):
        self.moons = moon.MoonSet()
