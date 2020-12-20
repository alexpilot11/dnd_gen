import random
import sys
from abc import abstractmethod, ABCMeta
from majormode.utils.namegen import NameGeneratorFactory


class PlanetAttribute(metaclass=ABCMeta):
    """Planet info base/helper class"""

    INDENT = 2
    ALIGNMENT = 40
    OUTER_DELIMITER = '\n'
    INNER_DELIMITER = '\n'

    # Extracts planet properties from derived classes
    @abstractmethod
    def __iter__(self):
        pass

    def __len__(self):
        return len(dict(self))

    def __str__(self):
        output = []
        for field, value in self:
            output.append(self._format_content(field, value))

        return self.OUTER_DELIMITER.join(output)

    @classmethod
    def _format_content(cls, label, content, alignment=None, indent=0, separator=':'):
        """Returns content as human-readable string"""

        if alignment is None:
            alignment = cls.ALIGNMENT

        if isinstance(content, PlanetAttribute):
            return cls._format_attribute(label, content, alignment, indent)
        elif isinstance(content, list):
            return cls._format_list(label, content, alignment, indent)
        else:
            return cls._format_field(label, content, alignment, indent, separator)

    @classmethod
    def _format_attribute(cls, label, attribute, alignment, indent):
        """Returns attribute as human-readable string"""

        output = []
        if len(attribute) == 1:
            dict_attribute = dict(attribute)
            label, item = list(dict_attribute.items())[0]
            output.append(cls._format_content(label, item, alignment, indent))
        elif len(attribute) > 1:
            output.append(cls._format_header(f'{label}', indent))
            for sub_label, item in attribute:
                output.append(cls._format_content(sub_label, item, alignment-cls.INDENT, indent+cls.INDENT))

        return cls.INNER_DELIMITER.join(output)

    @classmethod
    def _format_list(cls, label, items, alignment, indent):
        """Returns items as human-readable string"""

        output = []
        if len(items) == 1:
            output.append(cls._format_content(label, items[0], alignment, indent))
        elif len(items) > 1:
            output.append(cls._format_header(f'{label}', indent))
            for i in range(len(items)):
                output.append(cls._format_content('', items[i], alignment-cls.INDENT, indent+cls.INDENT, ''))

        return cls.INNER_DELIMITER.join(output)

    @classmethod
    def _format_header(cls, label, indent):
        """Returns a properly-indented header"""

        return f'{"":<{indent}}{label}'

    @classmethod
    def _format_field(cls, label, value, alignment, indent, separator=':'):
        """Returns a properly indented field and value"""

        return f'{"":<{indent}}{label+separator:<{alignment}}{value}'


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
        'A Few',
        'Occasional',
        'Frequent',
        'Unavoidable',
    )
    BLIGHT_TYPES = (
        'Spots',
        'Gashes',
        'Mountains',
        'Valleys',
        'Floating Structures',
        'Giant Oases',
        'Satellites',
        'Caves',
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
            yield 'Mainly', self.plane
            yield 'Deviation', f'{self.blight_frequency} {self.blight_type} of {self.blight}'
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
        if random.randint(1, 10) <= 3:
            self.economy = PlanetEconomy()
            self.size = random.choice(self.POPULATION_SIZES)
            self.conflict = PlanetConflict()
        else:
            self.economy = None
            self.size = None
            self.conflict = None

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
