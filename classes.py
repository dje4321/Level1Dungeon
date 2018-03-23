import uuid
from random import randint

class Player:
    def __init__(self, name):
        self.health = 100
        self.stamina = 50
        self.max_stamina = 100
        self.damage = 20
        self.damageVar = 20
        self.action = 'Preparing for Combat'
        self.name = name
        
class Enemy:
    def __init__(self):
        self.action = 'Saw Player'
        self.health = 100
        self.stamina = 20
        self.max_stamina = 30
        self.damage = 20
        self.damageVar = 10
        self.name = "Error Enemy"
        
        self.id = uuid.uuid4()
        
    def calcDamage(self):
        return randint(self.damage - self.damageVar, self.damage + self.damageVar)
        
    def guessLowDamage(self):
        return self.damage - randint(self.damageVar - 3, self.damageVar + 3)
        
    def guessHighDamage(self):
        return self.damage + randint(self.damageVar - 3, self.damageVar + 3)

class Zombie(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 125
        self.stamina = 10
        self.max_stamina = 15
        self.damage = 25
        self.damageVar = 10
        self.name = 'Zombie'
        
class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.health = 75
        self.stamina = 25
        self.max_stamina = 35
        self.damage = 15
        self.damageVar = 5
        self.name = 'Skeleton'
