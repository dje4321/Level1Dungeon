import uuid, os, sys, menu, time
from random import randint

class Player: # Main class for the player
    
    health = 100
    stamina = 50
    max_stamina = 100
    damage = 20
    damageVar = 10
    damageMod = 1
    action = 'Preparing for Combat'
    desc = 'Just a basic player'
    playerType = 'Basic'
    
    def __init__(self, name):
        self.name = name
    
    def checkHealth(self): # Checks to see if they player has died
        try:
            if self.health <= 0:
                os.system('clear')
                print('You join millions of others as your body wastes away')
                sys.exit()
        except Exception as e:
            print('classes.py - player.checkHealth')
            print('Exception:',e)
            input('Press enter to continue')
            
    def checkAction(self, enemys, action): # Checks what action the player has made 
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
                    print('classes.py - player.checkAction')
                    print('Exception:',e)
                    input('Press enter to continue')
       
        if action == '2': # Wait
            try:
                self.action = 'Waited'
                if self.stamina >= self.max_stamina:
                    os.system('clear')
                    print("You're already at max stamina")
                    input('Press enter to continue...')
                    return
                self.stamina += 5
                return
            except Exception as e:
                print('classes.py - player.checkAction')
                print('Exception:',e)
                input('Press enter to continue')
            
        if action == '3': # Display stats
            menu.displayStats(self,enemys)
        
        if action == '9': # Run Away
            self.action = 'Ran Away'
            os.system('clear')
            print('You manage to run away')
            sys.exit()
            
class Brute(Player):
    
    health = 120
    stamina = 30
    max_stamina = 60
    damage = 25
    damageVar = 15
    damageMod = 1
    desc = 'Your attacks are strong and powerful but unpredicable and tiring'
    playerType = 'Brute'
    
    def __init__(self, name):
        super().__init__(name)
    
class Agile(Player):
    
    health = 80
    stamina = 60
    max_stamina = 120
    damage = 15
    damageVar = 5
    damageMod = 1
    desc = 'Your attacks are weak but your strikes are predicable and frequent'
    playerType = 'Agile'
    
    def __init__(self, name):
        self.type = 'Agile'
        super().__init__(name)
        
class Enemy: # Base enemy class and traits
    num = 0
    
    action = 'Saw Player'
    health = 100
    stamina = 20
    max_stamina = 30
    damage = 20
    damageVar = 10
    damageMod = 0.5
    
    name = "Error Enemy"
    
    def __init__(self):        
        Enemy.num += 1
        self.id = uuid.uuid4()
        
    def calcDamage(self): # Calculates the amount of damage a enemy should do
        try:
            return int(randint(self.damage - self.damageVar, self.damage  + self.damageVar) * self.damageMod)
        
        except Exception as e:
            print('classes.py - enemy.calcDamage')
            print('Exception:',e)
            input('Press enter to continue')
            
    def guessLowDamage(self): # Will generate a approxomite low damage value
        return int((self.damage - randint(self.damageVar - 3, self.damageVar + 3)) * self.damageMod)
        
    def guessHighDamage(self): # Will generate a approxomite high damage value
        return int((self.damage + randint(self.damageVar - 3, self.damageVar + 3)) * self.damageMod)

class Zombie(Enemy): # Subclass Zombie
    health = 125
    stamina = 10
    max_stamina = 15
    damage = 25
    damageVar = 10
    name = 'Zombie'
    
    def __init__(self):
        super().__init__()
        
class Skeleton(Enemy): # Subclass Skeleton
    health = 75
    stamina = 25
    max_stamina = 35
    damage = 15
    damageVar = 5
    name = 'Skeleton'

    def __init__(self):
        super().__init__()
