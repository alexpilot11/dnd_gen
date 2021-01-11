import random

from majormode.utils.namegen import NameGeneratorFactory


class BaseEntity:
    OUTLINE = '-' * 40
    PADDING = '<25'


class Entity(BaseEntity):
    language = NameGeneratorFactory.Language.Greek

    def __init__(self):
        self.gen_name()

    @property
    def generate(self):
        return NameGeneratorFactory.get_instance(self.language).generate_name

    def print_attr(self, attr, value):
        print(f'{f"{attr}:":{self.PADDING}}{value}')

    def gen_name(self):
        word_count = random.choice([1]*3 + [2])  # Shorter names have higher weights
        self.name = ' '.join([self.generate() for _ in range(word_count)])
        if random.randint(0, 10) > 8:
            self.name += f' {random.choice(["I", "II", "III", "IV", "V"])}'
