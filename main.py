from classes.colors import BColors
from classes.character import Person
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic (offence)
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic (heal/defence)
cure = Spell("Cure", 12, 120, 'white')
resurrection = Spell("Resurrection", 18, 200, 'white')
player_spells = [fire, thunder, blizzard, meteor, cure, resurrection]

# Create Item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
high_potion = Item("High potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "potion", "Heals 200 HP", 200)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
mega_elixir = Item("MegaElixir", 'elixir', "Fully restores party's HP/MP", 9999)
grenade = Item("Grenade", 'attack', 'Deals 500 damage', 500)
player_items = [potion, high_potion, super_potion, elixir, mega_elixir, grenade]

# Instantiate people
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(BColors.FAIL + BColors.BOLD + 'AN ENEMY ATTACK!' + BColors.END_C)

while running:
    print('=' * 60)
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    if index == -1:
        continue

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(int(dmg))
        print('You attack for ', dmg, ' points of damage.')

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choice magic: ')) - 1
        if magic_choice == -1:
            continue
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(BColors.FAIL + "\nNot enough MP \n" + BColors.END_C)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(BColors.OK_BLUE + "\n" + spell.name + " health for " + str(magic_dmg) + ' HP.' + BColors.END_C)

        elif spell.type == 'black':
            enemy.take_damage(magic_dmg)
            print(BColors.OK_BLUE + " \n" + spell.name + " deals ", str(magic_dmg), "damage points of magic.\n",
                  BColors.END_C)
    elif index == 2:
        player.choose_items()
        item_choice = int(input('Choice item: ')) - 1
        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.kind == 'potion':
            player.heal(item.prop)
            print(BColors.OK_GREEN + '\n' + item.name + ' increase heals for ', str(item.prop) + 'HP' + BColors.END_C)

        elif item.kind == 'elixir':
            player.mp = player.max_mp
            player.hp = player.max_hp
            print(BColors.OK_GREEN + '\n' + item.name + ' fully restores HP/MP' + BColors.END_C)
        elif item.kind == "attack":
            enemy.take_damage(item.prop)
            print(BColors.WARNING + '\n' + item.name + ' enemy takes ',
                  str(item.prop) + ' damage points.' + BColors.END_C)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(int(enemy_dmg))
    print('Enemy attack for ', enemy_dmg, ' points of damage.')

    print("-" * 60)
    print('Enemy HP: ', BColors.FAIL, enemy.get_hp(), '/', enemy.get_max_hp(), BColors.END_C)
    print('Your HP: ', BColors.OK_GREEN, player.get_hp(), '/', player.get_max_hp(), BColors.END_C)
    print('Your MP: ', BColors.OK_BLUE, player.get_mp(), '/', player.get_max_mp(), BColors.END_C)
    print("-" * 60)

    if enemy.get_hp() == 0:
        print(BColors.OK_GREEN + 'You win!' + BColors.END_C)
        running = False

    elif player.get_hp() == 0:
        print(BColors.FAIL + 'You enemy has defeat you!' + BColors.END_C)
        running = False
