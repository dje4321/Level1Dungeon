import os, sys, function, AI, time

def mainLoop(player,enemys):
    
    while True:
        try:
            os.system('clear')
            
            print("You face {} enemys".format(len(enemys)))
            printEnemys(enemys)
            print("{}: Stamina:{} Health:{} Last Action: {}".format(player.name, player.stamina, player.health, player.action))
            print("")
           
            action = input('1.Attack 2.Wait 3.Display Stats 9.Run Away --> ')
            
            player.checkAction(enemys, action)
            AI.checkEnemyAction(player, enemys)
            
            player.checkHealth()
            function.checkEnemyHealth(enemys)
            function.winCondition(enemys)
            
        except Exception as e:
            pass

def printEnemys(enemys):
    for i in range(0,len(enemys)):
        print('''
        {} {}: Health:{} Stamina:{} Action: {}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].health, enemys[i].stamina, enemys[i].action))

def displayStats(player,enemys):
    os.system('clear')
    for i in range(0,len(enemys)):
        print('''
        {} {}: Appox Damage:{}-{} Health:{} Stamina:{} Max Stamina:{}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].guessLowDamage(), enemys[i].guessHighDamage(), enemys[i].health, enemys[i].stamina, enemys[i].max_stamina))
    print('')
    print('Player Stats: Damage:{}-{} Health:{} Stamina:{} Max Stamina:{}'.format(player.damage - player.damageVar, player.damage + player.damageVar, player.health, player.stamina, player.max_stamina))
    input('Please press enter...')

