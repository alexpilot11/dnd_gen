import random
import requests

from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import enums


class Planet:

    _generate = NameGeneratorFactory.get_instance(
        NameGeneratorFactory.Language.Greek
    ).generate_name
    OUTLINE = '-' * 40
    PADDING = '<25'


    def __init__(self):
        self.gen_plane()
        self.gen_name()
        self.gen_size()
        self.gen_plane()
        self.gen_population()
        self.gen_conflict()
        self.gen_raw_materials()
        self.gen_economy()

    def print_attr(self, attr, value):
        print(f'{f"{attr}:":{self.PADDING}}{value}')

    def display(self):
        print(self.OUTLINE)
        self.print_attr('Plane', self.plane.value)
        self.print_attr('Name', self.name)
        self.print_attr('Size', self.size.value)
        self.print_attr('Plane', self.plane.value)
        self.print_attr('Population', self.population.value)
        self.print_attr('Conflict', self.conflict.value)
        self.print_attr('Raw', self.raw_materials.value)
        self.print_attr('Economy', self.economy.value)
        print(self.OUTLINE)

    def gen_name(self):
        word_count = random.choice([1]*3 + [2])  # Shorter names have higher weights
        self.name = ' '.join([self._generate() for _ in range(word_count)])

    def gen_size(self):
        self.size = random.choice(list(enums.Size))

    def gen_plane(self):
        self.plane = random.choice(list(enums.Plane))

    def gen_population(self):
        self.population = random.choice(list(enums.Population))

    def gen_conflict(self):
        self.conflict = random.choice(list(enums.Conflict) + [enums.Conflict.NONE] * 5)

    def gen_raw_materials(self):
        self.raw_materials = random.choice(
            list(enums.RawMaterials) + [enums.RawMaterials.NONE] * 2
        )

    def gen_economy(self):
        self.economy = random.choice(list(enums.Economy) + [enums.RawMaterials.NONE])
