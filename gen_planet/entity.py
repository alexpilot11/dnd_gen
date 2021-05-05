import random

import roman
from majormode.utils.namegen import NameGeneratorFactory

from gen_planet import enums
from gen_planet.mixins import ParentMixin


class BaseEntity(ParentMixin):
    OUTLINE = '-' * 40
    PADDING = '<25'
    left_padding = '<0'
    language = NameGeneratorFactory.Language.Greek

    def __init__(self, num_children=None):
        self.num_children = num_children
        can_name_children_after_parent = (
            hasattr(self, 'parent') and not
            self.parent.children_named_after_parent
        ) or not hasattr(self, 'parent')
        self.children_named_after_parent = random.choice([can_name_children_after_parent, False])
        self.gen_name()

    @property
    def generate(self):
        return NameGeneratorFactory.get_instance(self.language).generate_name

    def gen_name(self):
        word_count = random.choice([1]*3 + [2])  # Shorter names have higher weights
        self.name = ' '.join([self.generate() for _ in range(word_count)])

    def print_attr(self, attr, value):
        print(f'{"":{self.left_padding}}{f"{attr}:":{self.PADDING}}{value}')


class BaseChildEntity(BaseEntity):
    left_padding = '<4'

    def __init__(self, parent, num_children=None):
        self.parent = parent
        super().__init__(num_children=num_children)

    def gen_name(self):
        if self.parent.children_named_after_parent:
            self.name = f'{self.parent.name} {roman.toRoman(self.parent.num_child)}'
            self.parent.num_child += 1
        else:
            super().gen_name()


class Entity(BaseChildEntity):
    is_colonized = False
    population = enums.Population.NONE
    conflict = enums.Conflict.NONE
    economy = enums.Economy.NONE

    def __init__(self, parent, num_children=None):
        super().__init__(parent, num_children=num_children)
        self.gen_plane()
        self.gen_size()
        self.gen_density()
        self.calc_gravity()
        self.gen_raw_materials()
        self.gen_population()

    def display(self):
        self.print_attr('Name', self.name)
        self.print_attr('Plane', self.plane.value)
        self.print_attr('Size', self.size.value)
        self.print_attr('Density', self.density.value)
        self.print_attr('Gravity', self.gravity.value)
        self.print_attr('Raw Materials', self.raw_materials.value)
        self.print_attr('Population', self.population.value)
        self.print_attr('Conflict', self.conflict.value)
        self.print_attr('Economy', self.economy.value)

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

    def gen_plane(self):
        self.plane = random.choice(list(enums.Plane))

    def gen_raw_materials(self):
        self.raw_materials = random.choice(
            list(enums.RawMaterials) + [enums.RawMaterials.NONE] * 2
        )

    def gen_population(self):
        choices = list(enums.Population)
        if self.size != enums.Size.GIANT:
            choices.remove(enums.Population.GIANT)

        self.population = random.choice(choices)
        if self.population.value is not None:
            self.gen_conflict()
            self.gen_economy()

    def gen_conflict(self):
        self.conflict = random.choice(list(enums.Conflict) + [enums.Conflict.NONE] * 5)

    def gen_economy(self):
        choices = list(enums.Economy) + [enums.Economy.NONE]
        if self.raw_materials is None:
            choices.remove(enums.Economy.RAW_MATERIALS)
        self.economy = random.choice(choices)
