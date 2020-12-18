import random
import requests
import sys


def gen_name():
    url = 'https://donjon.bin.sh/name/rpc-name.fcgi?type=Human+Male&n=10'
    resp = requests.get(url)
    names = resp.text.split('\n')
    choice = random.choice(names)
    return f'{"Name:":<20}{choice}'


def gen_size():
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
        'Crime',
        'None',
    ]
    choice = random.choice(economy)
    return f'{"Economy:":<20}{choice}'


def main(num):
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
    main(int(sys.argv[1]))
