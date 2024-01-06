import random


class Character:
    def __init__(self, name, health_points, max_attack, defense_points):
        self.name = name
        self.health_points = health_points
        self.max_attack = max_attack
        self.defense_points = defense_points
    
                
        
class Hero(Character):
    def __init__(self, name, health_points, max_attack, defense_points):
        super().__init__(name, health_points, max_attack, defense_points)
        self.level = 1
        self.experience = 0
        self.combo_strikes = {
            'double' : [], 
            'triple' : [],
        }
    
    def get_level(self):
        return self.level
    
    def attack(self, enemy):
        attack = random.randint(1*self.level, self.max_attack)
        dmg = attack - enemy.defense_points

        if len(self.combo_strikes['double']) >= 3:
            dmg = dmg * 2
            self.combo_strikes['double'] = []
            # print('Double Damage')

        if len(self.combo_strikes['triple']) >= 3:
            dmg = dmg * 3
            self.combo_strikes['triple'] = []
            # print('Triple Damage')

        if dmg > 0:
            print(f'Player [{self.name}] attacked enemy [{enemy.name}] with {dmg} damage                                      ', end='\r')
            enemy.health_points -= dmg
            if enemy.health_points <= 0:
                enemy.health_points = 0
                return

            if dmg < 3:
                self.combo_strikes['double'] = []
                self.combo_strikes['triple'] = []
            if dmg >= 3 and dmg < 5:
                self.combo_strikes['double'].append(dmg)
            else:
                self.combo_strikes['triple'].append(dmg)
        
        else:
            print('Your attack did not penetrate enemies armor ...                                                            ', end='\r')
            pass
    
    def add_experience(self, exp_amount):
        self.experience += exp_amount
        if self.experience >= self.level * 10:
            self.level_up() 
    
    def level_up(self):
        self.experience = 0
        self.level += 1
        print(f'Hero [{self.name}] level up !! Now at level {self.level}')


class Enemy(Character):
    def __init__(self, name, health_points, max_attack, defense_points, exp_drop):
        super().__init__(name, health_points, max_attack, defense_points)
        self.exp_drop = exp_drop
        self.dead = False
    
    def attack(self, hero):
        attack = random.randint(1*hero.level, self.max_attack*hero.level)
        dmg = attack - hero.defense_points

        if dmg > 0:
            print(f'Enemy [{self.name}] attacked hero [{hero.name}] with {dmg} damage                                         ', end='\r')
            hero.health_points -= dmg
        else:
            print(f'Enemy did not penetrate hero armor                                                                        ', end='\r')
            pass
    
    def stronger(self, hero_level):
        self.max_attack = self.max_attack * hero_level
        self.defense_points = self.defense_points * hero_level
        self.exp_drop = self.exp_drop * hero_level

    
    def is_dead(self):
        return self.dead
    
    def killed(self, hero_level):
        self.dead = True
        final_exp_drop = random.randint(1, self.exp_drop*hero_level)
        return final_exp_drop


if __name__ == '__main__':

    hero = Hero('Alex', 50, 10, 30)
    enemy = Enemy('Basic', 40, 1, 3)

    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)
    hero.attack(enemy)




