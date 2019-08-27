from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)

enemy = Person(1200, 65, 45, 25, magic)

running = True

print(BColors.FAIL + BColors.BOLD + 'AN ENEMY ATTACK!' + BColors.END_C)

while running:
    print('=========================')
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(int(dmg))
        print('You attack for ', dmg, ' points of damage. Enemy HP: ', enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(int(enemy_dmg))
    print('Enemy attack for ', enemy_dmg, ' points of damage. Player HP: ', player.get_hp())
    running = False
