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
        'Politial power struggle',
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


def main(num):
    # TODO: make should some planets have multiple "planets" inside of them?
    for i in range(num):
        print('-----------------------------------------')
        print(gen_name())
        print(gen_size())
        print(gen_plane())
        print(gen_gen_population())
        print(gen_conflict())
        print(gen_raw_materials())
        print(gen_economy())
        print('-----------------------------------------')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        num = 5
    elif len(sys.argv) == 2:
        num = int(sys.argv[1])
    else:
        raise Exception('too many args')
    main(num)
