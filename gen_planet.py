import math
import random
import sys
from abc import abstractmethod, ABCMeta
from majormode.utils.namegen import NameGeneratorFactory

class PlanetAttribute(metaclass=ABCMeta):
    INDENT = 2
    OUTER_DELIMITER = '\n'
    INNER_DELIMITER = '\n'

    # Extracts planet properties from derived classes
    @abstractmethod
    def __iter__(self):
        pass

    def __len__(self):
        return len(dict(self))

    def __str__(self):
        return self.format_attributes(*dict(self).items())

    @classmethod
    def format_attributes(cls, *attributes, alignment=40, indent=0):
        """Converts list of key value attributes to a human-readable string"""

        output = []
        for label, attribute in attributes:
            string = cls._format_attribute(label, attribute, alignment, indent)
            output.append(string)

        return cls.OUTER_DELIMITER.join(output)

    @classmethod
    def _format_attribute(cls, label, attribute, alignment, indent):
        output = []

        # Apply header and indentation if attribute has sub-items
        if len(attribute) > 1:
            output.append(f'{"":<{indent}}{label}')
            alignment -= cls.INDENT
            indent += cls.INDENT

        for field, value in attribute:
            if isinstance(value, PlanetAttribute):
                output.append(cls.format_attributes((field, value), alignment=alignment, indent=indent))
            else:
                output.append(cls._format_field(field, value, alignment, indent))

        return cls.INNER_DELIMITER.join(output)

    @classmethod
    def _format_field(cls, label, value, alignment, indent):
        return f'{"":<{indent}}{label+":":<{alignment}}{value}'

class PlanetName(PlanetAttribute):
    """Planet name generator"""

    _generate = NameGeneratorFactory.get_instance(NameGeneratorFactory.Language.Greek).generate_name
    max_length = 3

    def __init__(self):
        word_count = random.choice([1]*6 + [2]*3 + [3])  # Shorter names have higher weights
        self.name = ' '.join([self._generate() for _ in range(word_count)])

    def __iter__(self):
        yield 'Name', self.name


class PlanetSize(PlanetAttribute):
    """Planet size generator"""

    # TODO: make different percentages for planet sizes
    PLANET_SIZES = (
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    )

    def __init__(self):
        self.size = random.choice(self.PLANET_SIZES)

    def __iter__(self):
        yield 'Size', self.size


class PlanetPlane(PlanetAttribute):
    """Planet (dnd dimensional) plane generator"""

    PLANES = (
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
    )
    BLIGHT_FREQUENCIES = (
        'Single Instance',
        'Uncommon',
        'Common',
        'Always Nearby'
        'Unavoidable',
    )
    BLIGHT_TYPES = (
        'Spots',
        'Gashes',
        'Mountains',
        'Valleys',
        'Floating Formations',
        'Giant Oases',
        'Planetary Ring',
        'Subterranean',
    )

    def __init__(self):
        # Two random planes: one primary, and one secondary
        planes = random.sample(self.PLANES, 2)

        self.plane = planes[0]

        # Chance that the plane contains traces of another one
        if random.randint(1, 5) > 4:
            self.blight = planes[1]
            self.blight_type = random.choice(self.BLIGHT_TYPES)
            self.blight_frequency = random.choice(self.BLIGHT_FREQUENCIES)
        else:
            self.blight = None
            self.blight_type = None
            self.blight_frequency = None

    def __iter__(self):
        if self.blight is not None:
            yield 'Primarily', self.plane
            yield 'Blight Frequency', self.blight_frequency
            yield 'Blight Form', self.blight_type
            yield 'Blight', self.blight
        else:
            yield 'Plane', self.plane


class PlanetEconomy(PlanetAttribute):
    """Planet economy generator"""

    ECONOMIES = (
        'Raw materials',
        'Merchant',
        'Black market',
        'None',
    )

    def __init__(self):
        self.economy = random.choice(self.ECONOMIES)

    def __iter__(self):
        yield 'Economy', self.economy


class PlanetConflict(PlanetAttribute):
    """Planet conflict generator"""

    CONFLICT_TYPES = (
        'War',
        'Political land boundaries',
        'Citizen land boundaries',
        'Theft',
        'Crime - gangs',
        'Crime - slavery',
        'Crime - domestic abuse',
        'Political power struggle',
    )

    def __init__(self):
        self.conflict = random.choice(self.CONFLICT_TYPES)

    def __iter__(self):
        yield 'Conflict', self.conflict


class PlanetPopulation(PlanetAttribute):
    """Planet population generator"""

    # TODO: make different percentages for population sizes
    POPULATION_SIZES = (
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    )

    def __init__(self):
        self.economy = None
        self.conflict = None
        self.size = None
        self.races = None

        if random.randint(1, 10) <= 3:
            self.size = random.choice(self.POPULATION_SIZES)
            self.economy = PlanetEconomy()
            self.conflict = PlanetConflict()

    def __iter__(self):
        if self.size is None:
            yield 'Population Size', '<20'
        else:
            yield 'Size', self.size
            yield 'Economy', self.economy
            yield 'Conflict', self.conflict


class PlanetRawMaterials(PlanetAttribute):
    """Planet resources generator"""

    RAW_MATERIALS = (
        'Precious metal ore',
        'Precious gems',
        'Useful metal ore',
        'Vegetation',
        'Wood',
        'Magic metal',
        'Gas - medical',
        'Fuel - gas',
        'Fuel - coal-like',
    )

    def __init__(self):
        if random.randint(1, 10) <= 8:
            self.raw_materials = random.choice(self.RAW_MATERIALS)
        else:
            self.raw_materials = None

    def __iter__(self):
        yield 'Raw Materials', self.raw_materials


class Planet(PlanetAttribute):
    """Collection of planet attributes"""

    def __init__(self):
        # TODO: make should some planets have multiple "planets" inside of them?

        self.name = PlanetName()
        self.size = PlanetSize()
        self.plane = PlanetPlane()
        self.population = PlanetPopulation()
        self.raw_materials = PlanetRawMaterials()

    def __iter__(self):
        yield 'Name', self.name
        yield 'Size', self.size
        yield 'Plane', self.plane
        yield 'Population', self.population

        if self.raw_materials.raw_materials is not None:
            yield 'Raw Materials', self.raw_materials


class SolarSystem:
    """Collection of planets"""

    DELIMITER = f'\n{"-"*80}\n'

    def __init__(self, planet_count=5):
        self.planets = [Planet() for _ in range(planet_count)]

    def __str__(self):
        return self.DELIMITER.join(
            str(planet) for planet in self.planets
        )


def parse_args():
    if len(sys.argv) < 2:
        planet_count = 5
    elif len(sys.argv) == 2:
        planet_count = int(sys.argv[1])
    else:
        raise Exception('too many args')

    return planet_count


def main():
    planet_count = parse_args()
    solar_system = SolarSystem(planet_count)
    print(solar_system)


if __name__ == '__main__':
    main()
