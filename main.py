from source.characters import Hero, Enemy
import random
import time
import os


hero = Hero('Alex', health_points=50, max_attack=10, defense_points=30)

def create_suitable_enemies(hero):
    skeleton = Enemy('Skeleton', health_points=40, max_attack=1*hero.get_level(), defense_points=1*hero.get_level(), exp_drop=3*hero.get_level())
    grunt = Enemy('Grunt', health_points=60, max_attack=3*hero.get_level(), defense_points=2*hero.get_level(), exp_drop=5*hero.get_level())

    enemies = [skeleton, grunt]
    return enemies

def wait_and_clear_screen(wait=1):
    if wait != 0:
        time.sleep(wait)
    return_code = os.system('cls')
    if return_code != 0:
        return_code = os.system('clear')

def print_intro():
    print('Welcome to Codeira')
    print('-'*40)
    time.sleep(2)
    wait_and_clear_screen(5)


def print_hero_details(hero):
    print('Hero details')
    print('-'*40)
    print(f'[NAME] {hero.name}')
    print(f'[HP] {hero.health_points}')
    print(f'[LVL] {hero.get_level()}')
    print(f'[EXP] {hero.experience}')

def print_enemy_info(enemy):
    print('Enemy details')
    print('-'*40)
    print(f'[NAME] {enemy.name}')
    print(f'[HP] {enemy.health_points}')
    print(f'[AP] {enemy.max_attack}')
    print(f'[DP] {enemy.defense_points}')

def user_main_action():
    print_hero_details(hero)
    print()
    print('1) Walk\n2) Inventory (not implemented)\n3) Options (not implemented)\n4) Exit (not implemented)')
    action = input('Choose action (enter a number): ')
    return int(action)

def walk_the_walk():
    random_action = random.randint(1, 3)
    if random_action == 1 or random_action == 2:
        # TODO User fights with random enemy
        enemy = random.choice(create_suitable_enemies(hero))
        wait_and_clear_screen(2)
        print(f'Player [{hero.name}] has encountered enemy [{enemy.name}]')
        print_enemy_info(enemy)
        print()
        time.sleep(2)
        while not enemy.is_dead():
            if enemy.health_points <= 0:
                exp_gain = enemy.killed(hero.get_level())
                hero.add_experience(exp_gain)
                wait_and_clear_screen(0)
                print(f'Player wins the fight. Player gained {exp_gain} experience.')
                print()
                print_enemy_info(enemy)
                print()
                input('Press Enter to continue ...')
                wait_and_clear_screen(0)
                break
            hero.attack(enemy)
            time.sleep(0.5)
            enemy.attack(hero)
            print(f'Player [{hero.name}] has {hero.health_points} HP left and enemy has {enemy.health_points} HP left')
            

    elif random_action == 3:
        # TODO User walks without a fight
        print('Walks without a fight')
        wait_and_clear_screen(2)



print_intro()
while True:
    main_action = user_main_action()

    if main_action == 1:
        # TODO Walk the walk
        walk_the_walk()
    

    if main_action == 4:
        break


