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
