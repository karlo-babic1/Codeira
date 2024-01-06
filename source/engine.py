import os
import time
import random

from .characters import Hero, Enemy

def clear_scr():
    return_code = os.system('cls') # Try to clear screen for windows OS
    if return_code != 0: # If return code is not 0 (which means success)
        return_code = os.system('clear') # Then try to clear screen in linux OS

def print_intro():
    txt = f'''
        {"Welcome to Codeira !" : ^120}

        Once upon a time in the mystical land of Codeoria, a brave Python novice named Alex embarked on a quest to create their very own text-based RPG game. 
        Armed with the knowledge of basic Python syntax, 
        Alex opened their code editor and began crafting the epic tale of a hero's journey.

        As the protagonist ventured forth, facing mythical creatures and treacherous challenges, 
        Alex used conditional statements to create branching storylines. 
        
        Depending on the player's choices, they could encounter fierce dragons, solve puzzles, or forge alliances with mystical beings. 
        Each decision affected the outcome of the game, making it a truly personalized experience.
    '''
    for letter in txt:
        # In this example we use end='' to tell python no newline character after a print(which is deafult)
        # We also tell python to flush the output, otherwise it would wait for a buffer to fill up before printing to screen
        # This way we get a nice little animation at the start of a game

        # Uncomment the time.sleep() to get animation running
        print(letter, end='', flush=True) 
        # time.sleep(0.03)
    print()

    # These f-strings are really useful
    # We can make text go left, right, or to the center of a screen
    # You can use < for left-aligned, ^ for center-aligned and > for right-aligned
    print(f"{'---------------------------------------------------------------------------------------------' : ^140}") 
    input(f'{"Press Enter to continue ..." : ^120}')
    clear_scr()

def generate_healthbar(current_health, max_health, bar_width=20):
    full_char = chr(0x2593)
    empty_char = chr(0x2591)

    # Calculate the width of each unit of health
    unit_width = max_health / bar_width

    # Calculate the number of filled and empty characters
    filled_width = int(current_health / unit_width)
    empty_width = bar_width - filled_width

    # Generate the health bar string
    health_bar = f'{full_char * filled_width}{empty_char * empty_width}'

    return health_bar

def print_hero_details(hero):
    print(f"{'---------------------------------------------------------------------------------------------' : ^140}")
    print(f'{"HERO" : ^140}')
    print(f'{"Name: " + hero.name: ^140}')
    print(f'{"Health points: " + str(hero.health_points) : ^129}')
    print(f'{"Level: " + str(hero.level) : ^137}')
    print(f'{"Experience: " + str(hero.experience) : ^131}')
    print(f"{'---------------------------------------------------------------------------------------------' : ^140}")
    print()

def print_enemy_info(enemy):
    print(f"{'---------------------------------------------------------------------------------------------' : ^140}")
    print(f'{"ENEMY" : ^140}')
    print(f'{"Name: " + enemy.name: ^140}')
    print(f'{"Health points: " + str(enemy.health_points) : ^129}')
    print(f'{"Max Attack: " + str(enemy.max_attack) : ^137}')
    print(f'{"Armor: " + str(enemy.defense_points) : ^131}')
    print(f"{'---------------------------------------------------------------------------------------------' : ^140}")
    print()

def print_fight_status(hero, enemy, comment=''):
    clear_scr()
    dashed_line = f"{'-' * 140 : ^140}"

    hero_line = f'{"HERO" : ^70}' + f'{"ENEMY" : ^70}'
    name_line = f'{"Name: " + hero.name : ^70}' + f'{"Name: " + enemy.name : ^70}'
    healthbar_line = f'{str(generate_healthbar(hero.health_points, hero.max_hp)) : ^70}' + f'{str(generate_healthbar(enemy.health_points, enemy.max_hp)) : ^70}'
    health_line = f'{"Health points: " + str(hero.health_points) + " / " + str(hero.max_hp) : ^70}' + f'{"Health points: " + str(enemy.health_points) + " / " + str(enemy.max_hp) : ^70}'
    level_exp_line = f'{"Max Attack: " + str(hero.max_attack) : ^70}' + f'{"Max Attack: " + str(enemy.max_attack) : ^70}'
    armor_line = f'{"Armor: " + str(hero.defense_points) : ^70}' + f'{"Armor: " + str(enemy.defense_points) : ^70}'

    commentary_line = f"{comment : ^140}"

    combined_status = dashed_line + '\n' + hero_line + '\n' + healthbar_line + '\n' + name_line + '\n' + health_line + '\n' + level_exp_line + '\n' + armor_line + '\n' + dashed_line + '\n' + commentary_line+ '\n' + dashed_line
    print(combined_status, flush=True)



class GameEngine:
    def __init__(self) -> None:
        self.hero = Hero('Alex', health_points=50, max_attack=20, defense_points=5) # Create instance of our Hero
        self.enemy = None
        self.walk_fight_threshold = 0.8 # This is 80% chance that user will encounter a combat and 20% chance he will walk without a fight
    
    def create_enemies(self): # Create enemies and make them stronger according to Hero level
        skeleton = Enemy('Skeleton', health_points=40, max_attack=9, defense_points=5, exp_drop=4)
        grunt = Enemy('Grunt', health_points=60, max_attack=12, defense_points=6, exp_drop=9)

        enemies = [skeleton, grunt]
        ready_enemies = []
        for enemy in enemies:
            enemy.stronger(self.hero.level)
            ready_enemies.append(enemy)
        return ready_enemies
    
    def main_action(self):
        actions = {
            1: 'Walk',
            2: 'Inventory (not implemented)',
            3: 'Options (not implemented)',
            4: 'Exit'
        }
        print_hero_details(self.hero)
        print()
        for key, value in actions.items():
            print(f'{key}) {value}')
        action = input('Choose action (enter a number): ')
        return int(action)
    
    def walk(self):
        # Get a random float between 0 and 1 and set it as random_action
        random_action = random.random() 
        # We determine if the random_action is below or above the threshold
        if random_action <= self.walk_fight_threshold:
            # If random_action is below or equal to threshold
            # We create enemies and get a list of possible ones, then we pick one from the list
            self.enemy = random.choice(self.create_enemies())
            # Clear the screen
            clear_scr()
            # Print the encounter and enemy info
            print(f'Player [{self.hero.name}] has encountered enemy [{self.enemy.name}]')
            print()
            # Sleep for 2 seconds and start a fight
            time.sleep(2)
            self.fight_enemy()
            
            
        # If the random_action is above the threshold, we walk away for now
        elif random_action > self.walk_fight_threshold:
            # TODO User walks without a fight
            print('Walks without a fight')
            input('Press Enter to continue ...')
            clear_scr()
    
    def fight_enemy(self):
        # We create another loop for the fight
            while True:
                # We check if the hero has enough HP to continue fighting
                if self.hero.health_points <= 0:
                    print('You are dead !!')
                    break
                # Then we attack the enemy
                hero_damage = self.hero.attack(self.enemy)
                self.enemy.take_damage(hero_damage)
                if self.enemy.health_points <= 0:
                    # If the enemy HP drops to or below 0 we kill the enemy
                    # Enemy drops us (returns) experience for now, it will drop items and gold as well
                    exp_gain = self.enemy.killed(self.hero.level)
                    self.hero.add_experience(exp_gain)
                    print_fight_status(self.hero, self.enemy, comment=f'Player wins the fight. Player gained {exp_gain} experience.')
                    print()
                    input('Press Enter to continue ...')
                    clear_scr()
                    # We set the current enemy to None (as this one died)
                    self.enemy = None
                    # We break out of the inner "fight" loop and that gets us back at the "main menu" loop
                    break

                # If the enemy HP is not below or equal to 0 this code runs
                print_fight_status(self.hero, self.enemy, comment=f'[{self.hero.name}] > > > > > > > > > > > > > >  {hero_damage} DMG  > > > > > > > > > > > > > > [{self.enemy.name}]')
                # We pause the execution for 1 sec to make it more interesting
                time.sleep(1)
                # Then the enemy attacks hero
                enemy_damage = self.enemy.attack(self.hero)
                print_fight_status(self.hero, self.enemy, comment=f'[{self.hero.name}] < < < < < < < < < < < < < <  {enemy_damage} DMG  < < < < < < < < < < < < < < [{self.enemy.name}]')
                # Then we pause one more time
                time.sleep(1)
                

    def run_game(self):
        # Main game loop

        print_intro()
        while True:
            main_action = self.main_action()
            if main_action == 1:
                self.walk()

            elif main_action == 4:
                break
    
    

    
