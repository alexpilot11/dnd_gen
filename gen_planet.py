import random
import requests
import sys
from majormode.utils.namegen import NameGeneratorFactory


def gen_name():
    name_generator = NameGeneratorFactory.get_instance(NameGeneratorFactory.Language.Greek)
    return name_generator.generate_name()


def gen_size():
    # TODO: make different percentages for planet sizes
    sizes = [
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    ]
    choice = random.choice(sizes)
    return f'{"Size:":<20}{choice}'


def gen_plane():
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
    choice = random.choice(planes)
    return f'{"Plane:":<20}{choice}'


def gen_gen_population():
    # TODO: make different percentages for population sizes
    if random.randint(1, 10) > 3:
        return f'{"Population:":<20}None'

    population_sizes = [
        'Small',
        'Medium',
        'Large',
        'Huge',
        'Giant',
    ]
    choice = random.choice(population_sizes)
    return f'{"Population:":<20}{choice}'


def gen_conflict():
    if random.randint(1, 10) > 5:
        return f'{"Conflict:":<20}None'

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
    choice = random.choice(conflict_types)
    return f'{"Conflict:":<20}{choice}'


def gen_raw_materials():
    if random.randint(1, 10) > 8:
        return f'{"Raw materials:":<20}None'

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
    choice = random.choice(raw_materials)
    return f'{"Raw materials:":<20}{choice}'


def gen_economy():
    economy = [
        'Raw materials',
        'Merchant',
        'Black market',
        'None',
    ]
    choice = random.choice(economy)
    return f'{"Economy:":<20}{choice}'


class Planet:
    """Collection of planet attributes"""

    def __init__(self):
        pass

    def __str__(self):
        lines = [
            '-----------------------------------------',
            gen_name(),
            gen_size(),
            gen_plane(),
            gen_gen_population(),
            gen_conflict(),
            gen_raw_materials(),
            gen_economy(),
            '-----------------------------------------'
        ]

        return '\n'.join(fields)


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
        new_planet = Planet()
        print(new_planet)


if __name__ == '__main__':
    main(parse_args())
