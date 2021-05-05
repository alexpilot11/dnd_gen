from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import entity


class Moon(entity.Entity):
    language = NameGeneratorFactory.Language.Roman
    left_padding = '<8'


class MoonSet(entity.BaseEntity):
    left_padding = '<4'

    def __init__(self, parent, num_children=None):
        super().__init__(num_children)
        self.moons = []
        for i in range(parent.num_children):
            self.moons.append(Moon(parent))

    def display(self):
        print(f'{"":{self.left_padding}}Moons:')
        for moon in self.moons:
            print(f'{"":{self.left_padding}}{self.OUTLINE}')
            moon.display()
