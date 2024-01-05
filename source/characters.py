class Character:
    def __init__(self, name, health_points, attack_points, defense_points):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points
        self.combo_strikes = {
            'double' : [], 
            'triple' : [],
        }

    

    def attack(self, enemy):
        
        dmg = self.attack_points - enemy.defense_points
        print(self.combo_strikes)
        

        if len(self.combo_strikes['double']) >= 3:
            dmg = dmg * 2
            self.combo_strikes['double'] = []
            print('Double Damage')

        if len(self.combo_strikes['triple']) >= 5:
            dmg = dmg * 3
            self.combo_strikes['triple'] = []
            print('Triple Damage')

        if dmg > 0:
            enemy.health_points = enemy.health_points - dmg     
            print(f'You have attacked enemy with {dmg} dmg')
            print(f'Their current health points are {enemy.health_points}')
            # Razlika izmedu  helath_points i defense_points ???

            if dmg < 3:
                self.combo_strikes['double'] = []
                self.combo_strikes['triple'] = []
                print('None of special damage has been caused yet.')

            if dmg >= 3 and dmg < 5:
                self.combo_strikes['double'].append(dmg)
                print("Double damage!!")

            else:
                self.combo_strikes['triple'].append(dmg)
                print("Triple damage !!!!!!!!")
        
        if enemy.health_points == 0:
            print("You won!")
                
        
class Hero(Character):
    def __init__(self, name, health_points, attack_points, defense_points):
        super().__init__(name, health_points, attack_points, defense_points)
        print('change')


class Enemy(Character):
    def __init__(self, name, health_points, attack_points, defense_points):
        super().__init__(name, health_points, attack_points, defense_points)


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




