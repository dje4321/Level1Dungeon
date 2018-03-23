import uuid, os, sys, menu
from random import randint

class Player:
    def __init__(self, name):
        self.health = 100
        self.stamina = 50
        self.max_stamina = 100
        self.damage = 20
        self.damageVar = 10
        self.action = 'Preparing for Combat'
        self.name = name
    
    def checkHealth(self):
        if self.health <= 0:
            os.system('clear')
            print('You join millions of others as your body wastes away')
            sys.exit()
            
    def checkAction(self, enemys, action):
        if action == '1': # Attack
            while True:
                try:
                    os.system('clear')
                    if self.stamina <= 0:
                        print("You are too exhausted to attack")
                        time.sleep(3)
                        return
                    menu.printEnemys(enemys)
                    attack = int(input('What enemy do you want to attack? '))
                    self.action = 'Attacked {}'.format(enemys[attack - 1].name) 
                    enemys[attack - 1].health -= self.damage
                    self.stamina -= 5
                    return
                except Exception as e:
                    pass
       
        if action == '2': # Wait
            self.action = 'Waited'
            if self.stamina >= self.max_stamina:
                os.system('clear')
                print("You're already at max stamina")
                input('Press enter to continue...')
                return
            self.stamina += 5
            return
            
        if action == '3': # Display stats
            menu.displayStats(self,enemys)
        
        if action == '9': # Run Away
            self.action = 'Ran Away'
            os.system('clear')
            print('You manage to run away')
            sys.exit()
        
class Enemy:
    num = 0
    
    def __init__(self):
        self.action = 'Saw Player'
        self.health = 100
        self.stamina = 20
        self.max_stamina = 30
        self.damage = 20
        self.damageVar = 10
        self.name = "Error Enemy"
        
        Enemy.num += 1
        
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
