import os, sys, function, AI, time, classes
from random import randint


def mainLoop(player,enemys): # main game loop
    wave = 1 #Defines starting wave
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
        print('Player Stats: Damage:{}-{} Health:{} Stamina:{} Max Stamina:{} Type:{}'.format(player.damage - player.damageVar, player.damage + player.damageVar, player.health, player.stamina, player.max_stamina, player.playerType)) # Prints the players stats
        input('Please press enter...')
    except Exception as e:
        print('menu.py - displayStats')
        print('Exception:',e)
        input('Press enter to continue')

def choosePlayer():
    try:
        os.system('clear')
        name = input('Please enter your name: ')
        os.system('clear')
        print('''
        1. Basic Player: Damage:{} Damage Varience:{} Health:{} Stamina:{} Max Stamina:{} Desc:{}
        '''.format(classes.Player.damage, classes.Player.damageVar, classes.Player.health, classes.Player.stamina, classes.Player.max_stamina, classes.Player.desc))
        print('''
        2. Brute: Damage:{} Damage Varience:{} Health:{} Stamina:{} Max Stamina:{} Desc:{}
        '''.format(classes.Brute.damage, classes.Brute.damageVar, classes.Brute.health, classes.Brute.stamina, classes.Brute.max_stamina, classes.Brute.desc))
        print('''
        3. Agile: Damage:{} Damage Varience:{} Health:{} Stamina:{} Max Stamina:{} Desc:{}
        '''.format(classes.Agile.damage, classes.Agile.damageVar, classes.Agile.health, classes.Agile.stamina, classes.Agile.max_stamina, classes.Agile.desc))
        action = input("Please select your class: ")
        if action == '1':
            player = classes.Player(str(name))
        if action == '2':
            player = classes.Brute(str(name))
        if action == '3':
            player = classes.Agile(str(name))
        return player
        
    except Exception as e:
        print('menu.py - choosePlayer')
        print('Exception:',e)
        input('Press enter to continue')
