class Character:
    def __init__(self, name, health_points, attack_points, defense_points):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points
        self.defense_points = defense_points

    def attack(self, enemy):
        diff = self.attack_points - enemy.defense_points

        if diff > 0:
            enemy.health_points - diff     
            print(f'You have attacked enemy with {diff} damage')


class Hero(Character):
    def __init__(self, name, health_points, attack_points, defense_points):
        super().__init__(name, health_points, attack_points, defense_points)


class Enemy(Character):
    def __init__(self, name, health_points, attack_points, defense_points):
        super().__init__(name, health_points, attack_points, defense_points)


hero = Hero('Alex', 50, 10, 30)
enemy = Enemy('Basic', 40, 1, 3)

hero.attack(enemy)




