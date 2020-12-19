import random
import sys
from majormode.utils.namegen import NameGeneratorFactory


class PlanetAttribute:
    """Planet quality/attribute helper class"""

    delimiter = '\n'
    indent = 4

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    @classmethod
    def format_attributes(cls, name, value, alignment=20, indent=0):
        """Pretty print attributes"""

        if isinstance(value, dict):
            return cls._format_dict(name, value, alignment, indent)
        else:
            return cls._format_attribute(name, value, alignment, indent)

    @classmethod
    def _format_dict(cls, name, values, alignment=20, indent=0):
        output = [f'{"":<{indent}}{name}']
        for k, v in values.items():
            output.append(
                cls.format_attributes(k, v, alignment + cls.indent, indent + cls.indent)
            )
        return cls.delimiter.join(output)

    @classmethod
    def _format_attribute(cls, name, value, alignment=20, indent=0):
        return f'{"":<{indent}}{name + ":":<{alignment}}{value}'


class PlanetName(PlanetAttribute):
    """Planet name generator"""

    _generate = NameGeneratorFactory.get_instance(NameGeneratorFactory.Language.Greek).generate_name
    max_length = 3

    def __init__(self):
        word_count = random.choice([1]*6 + [2]*3 + [3])  # Shorter names have higher weights
        super().__init__(' '.join([self._generate() for _ in range(word_count)]))


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
        super().__init__(random.choice(self.PLANET_SIZES))


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

    def __init__(self):
        super().__init__(random.choice(self.PLANES))


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
        planet_size = '<20'
        if random.randint(1, 10) <= 3:
            planet_size = random.choice(self.POPULATION_SIZES)

        super().__init__(planet_size)


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
        conflict = 'None'
        if random.randint(1, 10) <= 5:
            conflict = random.choice(self.CONFLICT_TYPES)

        super().__init__(conflict)


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
        raw_materials = 'None'
        if random.randint(1, 10) <= 8:
            raw_materials = random.choice(self.RAW_MATERIALS)

        super().__init__(raw_materials)


class PlanetEconomy(PlanetAttribute):
    """Planet economy generator"""

    ECONOMIES = (
        'Raw materials',
        'Merchant',
        'Black market',
        'None',
    )

    def __init__(self):
        super().__init__(random.choice(self.ECONOMIES))


class Planet:
    """Collection of planet attributes"""

    def __init__(self):
        # TODO: make should some planets have multiple "planets" inside of them?

        self.attributes = {
            'Name': PlanetName(),
            'Size': PlanetSize(),
            'Plane': PlanetPlane(),
            'Population': PlanetPopulation(),
            'Conflict': PlanetConflict(),
            'Raw Materials': PlanetRawMaterials(),
            'Economy': PlanetEconomy(),
        }

    def __str__(self):
        return PlanetAttribute.format_attributes('Planet', self.attributes)


class SolarSystem:
    """Collection of planets"""

    delimiter = f'\n{"-"*40}\n'

    def __init__(self, planet_count=5):
        self.planets = [Planet() for _ in range(planet_count)]

    def __str__(self):
        return self.delimiter.join(
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
