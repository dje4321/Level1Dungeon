import uuid

class Player:
    def __init__(self, name):
        self.health = 20
        self.stamina = 10
        self.max_stamina = 20
        self.damage = 5
        self.action = 'Preparing for Combat'
        self.name = name
        
class Enemy:
    def __init__(self):
        self.action = 'Saw Player'
        self.health = 10
        self.stamina = 10
        self.max_stamina = 20
        self.damage = 0
        self.name = "Error Enemy"
        
        self.id = uuid.uuid4()
        
        def death(self,enemy):
            if enemy in self.Enemy:
                self.enemy.remove()

class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 15
        self.stamina = 0
        self.max_stamina = 5
        self.damage = 5
        self.name = 'Zombie'
        
class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 10
        self.stamina = 5
        self.max_stamina = 5
        self.damage = 8
        self.name = 'Skeleton'
