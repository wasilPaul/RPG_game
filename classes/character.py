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
        hp_bar_length = 25
        hp_bar = ''
        hp_bar_ticks = self.hp / self.max_hp * 100 / 4

        mp_bar_length = 10
        mp_bar = ''
        mp_bar_ticks = self.mp / self.max_mp * 100 / 10

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < hp_bar_length:
            hp_bar += ' '

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < mp_bar_length:
            mp_bar += " "

        hp_quantity = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_quantity) < 10:
            decrease = 10 - len(hp_quantity)
            current_hp = decrease * " " + hp_quantity

        mp_quantity = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""
        if len(mp_quantity) < 10:
            decrease = 10 - len(mp_quantity)
            current_mp = decrease * " " + mp_quantity

        if len(self.name) < 10:
            decrease = 10 - len(self.name)
            name_section = self.name + decrease * " "
        elif len(self.name) > 10:
            name_section = self.name[0:7] + "..."
        else:
            name_section = self.name

        print(
            BColors.BOLD + name_section + " : " + current_hp + BColors.OK_GREEN + " |" + hp_bar + "| " + BColors.END_C + BColors.BOLD + current_mp + BColors.OK_BLUE + " |" + mp_bar + "|" + BColors.END_C)

    def get_enemy_stats(self):
        max_bar_tics = 50
        hp_bar = ''
        hp_bar_ticks = self.hp / self.max_hp * 100 / 2

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < max_bar_tics:
            hp_bar += ' '

        hp_quantity = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_quantity) < 10:
            decrease = 10 - len(hp_quantity)

            current_hp = decrease * " " + hp_quantity

        if len(self.name) < 10:
            decrease = 10 - len(self.name)
            name_section = self.name + decrease * " "
        elif len(self.name) > 10:
            name_section = self.name[0:7] + "..."
        else:
            name_section = self.name

        print(
            BColors.BOLD + name_section + " : " + current_hp + BColors.FAIL + " |" + hp_bar + "| " + BColors.END_C)
