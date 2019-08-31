import random
from .colors import BColors
from .magic import Spell


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

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
        print(BColors.BOLD + self.name + BColors.END_C)
        print(BColors.OK_BLUE + BColors.BOLD + "ACTIONS:" + BColors.END_C)
        for item in self.actions:
            print(" " * 3, str(i) + ". ", item)
            i += 1

    def choose_magic(self):
        i = 1
        print('\n', BColors.OK_BLUE + BColors.BOLD + "MAGIC:" + BColors.END_C)
        for spell in self.magic:
            print(" " * 3, str(i) + ". ", spell.name, "(cost: ", str(spell.cost), ")")
            i += 1

    def choose_items(self):
        i = 1
        print('\n', BColors.OK_GREEN + BColors.BOLD + 'ITEMS:' + BColors.END_C)
        for item in self.items:
            print(" " * 3, str(i) + '. ' + item['item'].name, ": ",
                  item['item'].description + " (x " + str(item['quantity']) + ")")
            i += 1

    def get_stats(self):
        print(BColors.BOLD + self.name + ": " + str(self.hp) + "/" + str(
            self.max_hp) + BColors.OK_GREEN + " |" + "█" * 25 + "| " + BColors.END_C + BColors.BOLD + str(
            self.mp) + "/" + str(
            self.max_mp) + BColors.OK_BLUE + " |" + "█" * 10 + "|" + BColors.END_C)
