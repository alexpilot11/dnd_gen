import random

from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import enums, moon
from gen_planet.entity import Entity


class Planet(Entity):
    def __init__(self):
        super().__init__()
        self.gen_name()
        self.gen_plane()
        self.gen_size()
        self.gen_raw_materials()
        if self.is_colonized:
            self.gen_population()
        self.gen_moons()

    def display(self):
        print(self.OUTLINE)
        self.print_attr('Name', self.name)
        self.print_attr('Plane', self.plane.value)
        self.print_attr('Size', self.size.value)
        self.print_attr('Density', self.density.value)
        self.print_attr('Gravity', self.gravity.value)
        self.print_attr('Raw Materials', self.raw_materials.value)
        self.print_attr('Population', self.population.value)
        self.print_attr('Conflict', self.conflict.value)
        self.print_attr('Economy', self.economy.value)
        self.moons.display()
        print(self.OUTLINE)

    def gen_plane(self):
        self.plane = random.choice(list(enums.Plane))

    def gen_raw_materials(self):
        self.raw_materials = random.choice(
            list(enums.RawMaterials) + [enums.RawMaterials.NONE] * 2
        )

    def gen_population(self):
        choices = list(enums.Population)
        if self.size != enums.Size.GIANT:
            choices.remove(enums.Population.GIANT)

        self.population = random.choice(choices)
        if self.population.value is not None:
            self.gen_conflict()
            self.gen_economy()

    def gen_conflict(self):
        self.conflict = random.choice(list(enums.Conflict) + [enums.Conflict.NONE] * 5)

    def gen_economy(self):
        choices = list(enums.Economy) + [enums.Economy.NONE]
        if self.raw_materials is None:
            choices.remove(enums.Economy.RAW_MATERIALS)
        self.economy = random.choice(choices)

    def gen_moons(self):
        self.moons = moon.MoonSet()
