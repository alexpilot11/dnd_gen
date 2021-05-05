import random

from gen_planet.entity import BaseEntity
from gen_planet.planet import Planet


class SolarSystem(BaseEntity):
    def __init__(self, num_children):
        super().__init__(num_children)
        self.planets = [Planet(self, num_children=random.randint(0, 6)) for i in range(num_children)]

    def display(self):
        print(self.name)
        for planet in self.planets:
            planet.display()
