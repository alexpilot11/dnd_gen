import random
import sys
from abc import ABCMeta, abstractmethod
from majormode.utils.namegen import NameGeneratorFactory


class PlanetAttribute(metaclass=ABCMeta):
    string_padding = 20

    @property
    @abstractmethod
    def attribute_name(self):
        pass

    def __init__(self):
        self.name = self.attribute_name
        self.value = self.generate()

    def __str__(self):
        return f'{self.name+":":<{self.string_padding}}{self.value}'

    @classmethod
    @abstractmethod
    def generate(cls):
        pass


class PlanetName(PlanetAttribute):
    attribute_name = 'Name'
    _generate_planet_name = NameGeneratorFactory.get_instance(NameGeneratorFactory.Language.Greek).generate_name

    @classmethod
    def generate(cls):
        return cls._generate_planet_name()


class PlanetSize(PlanetAttribute):
    attribute_name = 'Size'

    # TODO: make different percentages for planet sizes
    planet_sizes = [
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    ]

    @classmethod
    def generate(cls):
        return random.choice(cls.planet_sizes)


class PlanetPlane(PlanetAttribute):
    attribute_name = 'Plane'
    planes = [
        'Material',
        'Feywild',
        'Shadowfell',
        'Mechanus',
        'Limbo',
        'Pandemonium',
        'The Abyss',
        'Carceri',
        'Hades',
        'Gehenna',
        'The Nine Hells',
        'Acheron',
        'Arcadia',
        'Mount Celestia',
        'Bytopia',
        'Elysium',
        'The Beastlands',
        'Arborea',
        'Ysgard',
    ]

    @classmethod
    def generate(cls):
        return random.choice(cls.planes)


class PlanetPopulation(PlanetAttribute):
    attribute_name = 'Population'
    # TODO: make different percentages for population sizes
    population_sizes = [
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    ]

    @classmethod
    def generate(cls):
        if random.randint(1, 10) > 3:
            return '<20'
        else:
            return random.choice(cls.population_sizes)


class PlanetConflict(PlanetAttribute):
    attribute_name = 'Conflict'
    conflict_types = [
        'War',
        'Political land boundaries',
        'Citizen land boundaries',
        'Theft',
        'Crime - gangs',
        'Crime - slavery',
        'Crime - domestic abuse',
        'Political power struggle',
    ]

    @classmethod
    def generate(cls):
        if random.randint(1, 10) > 5:
            return 'None'
        else:
            return random.choice(cls.conflict_types)


class PlanetRawMaterials(PlanetAttribute):
    attribute_name = 'Raw Materials'
    raw_materials = [
        'Precious metal ore',
        'Precious gems',
        'Useful metal ore',
        'Vegetation',
        'Wood',
        'Magic metal',
        'Gas - medical',
        'Fuel - gas',
        'Fuel - coal-like',
    ]

    @classmethod
    def generate(cls):
        if random.randint(1, 10) > 8:
            return 'None'
        else:
            return random.choice(cls.raw_materials)


class PlanetEconomy(PlanetAttribute):
    attribute_name = 'Economy'
    economy = [
        'Raw materials',
        'Merchant',
        'Black market',
        'None',
    ]

    @classmethod
    def generate(cls):
        return random.choice(cls.economy)


class Planet:
    """Collection of planet attributes"""

    def __init__(self):
        self.name = PlanetName()
        self.size = PlanetSize()
        self.plane = PlanetPlane()
        self.population = PlanetPopulation()
        self.conflict = PlanetConflict()
        self.raw_materials = PlanetRawMaterials()
        self.economy = PlanetEconomy()

    def __str__(self):
        return '\n'.join([
            str(self.name),
            str(self.size),
            str(self.plane),
            str(self.population),
            str(self.conflict),
            str(self.raw_materials),
            str(self.economy),
        ])


def parse_args():
    if len(sys.argv) < 2:
        planet_count = 5
    elif len(sys.argv) == 2:
        planet_count = int(sys.argv[1])
    else:
        raise Exception('too many args')

    return planet_count


def main(planet_count):
    # TODO: make should some planets have multiple "planets" inside of them?
    for i in range(planet_count):
        print('-----------------------------------------')
        print(Planet())
        print('-----------------------------------------')


if __name__ == '__main__':
    main(parse_args())
