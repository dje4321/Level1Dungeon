from random import randint
import classes, os, sys, time, menu

def randEnemy(numEnemy,enemys='None'):
    if enemys == 'None':
        enemys = []
        
    for i in range(0,numEnemy):
        randNum = randint(0,1)
        if randNum == 0:
            enemys.append(classes.Zombie())
        if randNum == 1:
            enemys.append(classes.Skeleton())
            
    return enemys

def checkPlayerAction(player, enemys, action):
    action = int(action)
    if action == 1: # Attack
        while True:
            try:
                os.system('clear')
                if player.stamina <= 0:
                    print("You are too exhausted to attack")
                    time.sleep(3)
                    return
                menu.printEnemys(enemys)
                attack = input('What enemy do you want to attack? ')
                player.action = 'Attacked {}'.format(enemys[int(attack) - 1].name) 
                enemys[int(attack) - 1].health -= player.damage
                player.stamina -= 5
                return
            except Exception as e:
                pass
    if action == 2: # Wait
        player.action = 'Waited'
        if player.stamina >= player.max_stamina:
            os.system('clear')
            print("You're already at max stamina")
            time.sleep(3)
            return
        player.stamina += 5
        return
    if action == 9: # Run Away
        player.action = 'Ran Away'
        os.system('clear')
        print('You manage to run away')
        sys.exit()

def checkPlayerHealth(player):
    if player.health <= 0:
        os.system('clear')
        print('You join millions of others as your body wastes away')
        sys.exit()

def checkEnemyHealth(enemys):
    i = 0
    while i < len(enemys):
        if enemys[i].health <= 0:
            enemys.pop(i)
        i += 1
    return enemys

def winCondition(enemys):
    if len(enemys) == 0:
        os.system('clear')
        print('Congrats. You win :D')
        sys.exit()
