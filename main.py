from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True

print(BColors.FAIL + BColors.BOLD + 'AN ENEMY ATTACK!' + BColors.END_C)

while running:
    print('=' * 60)
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(int(dmg))
        print('You attack for ', dmg, ' points of damage.')
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choice magic: ')) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        current_mp = player.get_mp()
        if cost > current_mp:
            print(BColors.FAIL + "\nNot enough MP \n" + BColors.END_C)
            continue
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(BColors.OK_BLUE + " \n" + spell + " deals ", str(magic_dmg), "damage points of magic.\n", BColors.END_C)

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
