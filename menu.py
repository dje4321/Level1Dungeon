import os, sys, function, AI, time
from random import randint


def mainLoop(player,enemys): # main game loop
    wave = 300 #Defines starting wave
    for i in range(0,len(enemys)):
                    enemys[i].damageMod = 0.5 * wave #Runs through enemies and syncs the damageMod value to the starting wave
    while True:
        try:
            os.system('clear') #Clear screen
            
            print("Wave:{} You face {} enemys".format(wave,len(enemys))) #P rints the main screen 
            printEnemys(enemys)
            print("{}: Stamina:{} Health:{} Last Action: {}".format(player.name, player.stamina, player.health, player.action))
            print("")
           
            action = input('1.Attack 2.Wait 3.Display Stats 9.Run Away --> ') # Promts the player menu
            
            player.checkAction(enemys, action) # Checks for what action the player has done
            AI.checkEnemyAction(player, enemys) # Checks the AI for their action
            
            player.checkHealth() # Checks the player's health
            function.checkEnemyHealth(enemys) # Checks to see if any enemies has died
            
            if len(enemys) <= 0: # Checks to see if the wave is over and will generate more enemys 
                enemys = function.randEnemy(randint(1,3),enemys)
                wave += 1
                for i in range(0,len(enemys)):
                    enemys[i].damageMod = 0.5 * wave
            
        except Exception as e:
            print('menu.py - mainLoop')
            print('Exception:',e)
            input('Press enter to continue')

def printEnemys(enemys): # Prints a list of enemies
    for i in range(0,len(enemys)):
        print('''
        {} {}: Health:{} Stamina:{} Action: {}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].health, enemys[i].stamina, enemys[i].action))

def displayStats(player,enemys):
    try:
        os.system('clear')
        for i in range(0,len(enemys)): # Prints enemys stats 
            print('''
            {} {}: Appox Damage:{}-{} Health:{} Stamina:{} Max Stamina:{}
            '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].guessLowDamage(), enemys[i].guessHighDamage(), enemys[i].health, enemys[i].stamina, enemys[i].max_stamina))
        print('')
        print('Player Stats: Damage:{}-{} Health:{} Stamina:{} Max Stamina:{}'.format(player.damage - player.damageVar, player.damage + player.damageVar, player.health, player.stamina, player.max_stamina)) # Prints the players stats
        input('Please press enter...')
    except Exception as e:
        print('menu.py - displayStats')
        print('Exception:',e)
        input('Press enter to continue')

