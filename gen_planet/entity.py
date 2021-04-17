import random

from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import enums


class BaseEntity:
    OUTLINE = '-' * 40
    PADDING = '<25'


class Entity(BaseEntity):
    language = NameGeneratorFactory.Language.Greek
    left_padding = '<0'
    is_colonized = False
    population = enums.Population.NONE
    conflict = enums.Conflict.NONE
    economy = enums.Economy.NONE

    def __init__(self):
        self.gen_name()
        self.gen_size()
        self.gen_density()
        self.calc_gravity()

    @property
    def generate(self):
        return NameGeneratorFactory.get_instance(self.language).generate_name

    def print_attr(self, attr, value):
        print(f'{"":{self.left_padding}}{f"{attr}:":{self.PADDING}}{value}')

    def gen_name(self):
        word_count = random.choice([1]*3 + [2])  # Shorter names have higher weights
        self.name = ' '.join([self.generate() for _ in range(word_count)])
        if random.randint(0, 10) > 8:
            self.name += f' {random.choice(["I", "II", "III", "IV", "V"])}'

    def gen_size(self):
        self.size = random.choice(list(enums.Size))

    def gen_density(self):
        self.density = random.choice(list(enums.Density))

    def calc_gravity_score(self):
        if self.size == enums.Size.SMALL:
            size = 1
        elif self.size == enums.Size.MEDIUM:
            size = 3
        elif self.size == enums.Size.LARGE:
            size = 5
        elif self.size == enums.Size.HUGE:
            size = 7
        else:
            size = 9

        if self.density == enums.Density.LOW:
            density = 1
        elif self.density == enums.Density.MEDIUM:
            density = 3
        else:
            density = 5

        return size * density

    def calc_gravity(self):
        score = self.calc_gravity_score()
        if score < 5:
            self.gravity = enums.Gravity.VERY_LIGHT
        elif score < 13:
            self.gravity = enums.Gravity.LIGHT
        elif score < 23:
            self.gravity = enums.Gravity.MEDIUM
        elif score < 35:
            self.gravity = enums.Gravity.HEAVY
        elif score <= 45:
            self.gravity = enums.Gravity.VERY_HEAVY
