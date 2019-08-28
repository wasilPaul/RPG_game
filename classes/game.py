import random
from .colors import BColors
from .magic import Spell


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(BColors.OK_BLUE + BColors.BOLD + "Actions" + BColors.END_C)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(BColors.OK_BLUE + BColors.BOLD + "Magic" + BColors.END_C)
        for spell in self.magic:
            print(str(i) + ":", spell.name, "(cost: ", str(spell.cost), ")")
            i += 1
