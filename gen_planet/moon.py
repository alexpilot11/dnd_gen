import random

from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import entity


class Moon(entity.Entity):
    language = NameGeneratorFactory.Language.Roman
    left_padding = 4

    def display(self):
        self.print_attr(f'{"":{self.left_padding}}Name', self.name)


class MoonSet(entity.BaseEntity):
    def __init__(self):
        self.moons = []
        for i in range(random.randint(0, 6)):
            self.moons.append(Moon())

    def display(self):
        print('Moons:')
        for moon in self.moons:
            print(self.OUTLINE)
            moon.display()
