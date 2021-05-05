import random

from gen_planet.solar_system import SolarSystem


def main(num):
    for i in range(num):
        solar_system = SolarSystem(random.randint(1,5))
        solar_system.display()
