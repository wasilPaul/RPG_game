from classes.colors import BColors
from classes.character import Person
from classes.magic import Spell
from classes.inventory import Item
import random

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
mega_elixir = Item("MegaElixir", 'elixir', "All team fully restores party's HP/MP", 9999)
grenade = Item("Grenade", 'attack', 'Deals 500 damage', 500)
player_items = [{"item": potion, "quantity": 10}, {"item": high_potion, "quantity": 5},
                {"item": super_potion, "quantity": 1}, {"item": elixir, "quantity": 1},
                {"item": mega_elixir, "quantity": 1}, {"item": grenade, "quantity": 5}]

# Instantiate people
player1 = Person("Niko", 4600, 500, 160, 340, player_spells, player_items)
player2 = Person("Kira", 460, 65, 100, 50, player_spells, player_items)
player3 = Person("Xio-Xi-Xen", 460, 80, 70, 80, player_spells, player_items)
players = [player1, player2, player3]

enemy1 = Person("Mag", 9200, 200, 300, 25, [], [])
enemy2 = Person("Brutal", 2200, 65, 150, 25, [], [])
enemy3 = Person("Brutal", 2200, 65, 150, 25, [], [])
enemies = [enemy1, enemy2, enemy3]
running = True

print(BColors.FAIL + BColors.BOLD + 'AN ENEMY ATTACK!' + BColors.END_C)

while running:
    print('=' * 60)

    for player in players:
        player.get_stats()

    print("-" * 60)
    for enemy in enemies:
        enemy.get_enemy_stats()

    print("-" * 60)
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1
        if index == -1:
            continue

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(int(dmg))
            print('\nYou attack' + enemies[enemy].name + ' for ' + str(dmg) + ' points of damage.')

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
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(
                    BColors.OK_BLUE + " \n" + spell.name + " deals " + str(magic_dmg) + " damage points of magic, to " +
                    enemies[enemy].name + BColors.END_C)
        elif index == 2:
            player.choose_items()
            item_choice = int(input('Choice item: ')) - 1
            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']

            if player.items[item_choice]['quantity'] == 0:
                print(BColors.FAIL + '\n' + 'None ' + item.name + " left ... " + BColors.END_C)
                continue

            player.items[item_choice]['quantity'] -= 1

            if item.kind == 'potion':
                player.heal(item.prop)
                print(BColors.OK_GREEN + '\n' + item.name + ' increase heals for ' + str(
                    item.prop) + ' HP' + BColors.END_C)

            elif item.kind == 'elixir':
                if item.name == 'MegaElixir':
                    for play in players:
                        play.mp = play.max_mp
                        play.hp = play.max_hp
                else:
                    player.mp = player.max_mp
                    player.hp = player.max_hp
                print(BColors.OK_GREEN + '\n' + item.name + ' fully restores HP/MP' + BColors.END_C)

            elif item.kind == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(BColors.FAIL + '\n' + item.name + ' enemy ' + enemies[enemy].name + ' takes ',
                      str(item.prop) + ' damage points.' + BColors.END_C)

    enemy_choice = 1
    enemy_dmg = enemies[0].generate_damage()
    enemy_target = random.randrange(0, len(players))
    players[enemy_target].take_damage(int(enemy_dmg))
    print('Enemy attack ' + players[enemy_target].name + ' for ', enemy_dmg, ' points of damage.')

    if enemy.get_hp() == 0:
        print(BColors.OK_GREEN + 'You win!' + BColors.END_C)
        running = False

    elif player.get_hp() == 0:
        print(BColors.FAIL + 'You enemy has defeat you!' + BColors.END_C)
        running = False
