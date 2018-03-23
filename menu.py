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
            
            function.checkPlayerAction(player, enemys, action)
            AI.checkEnemyAction(player, enemys)
            
            function.checkPlayerHealth(player)
            function.checkEnemyHealth(enemys)
            function.winCondition(enemys)
            
        except Exception as e:
            print('Somehow hit a error: {}'.format(e))
            time.sleep(3)

def printEnemys(enemys):
    for i in range(0,len(enemys)):
        print('''
        {} {}: Health:{} Stamina:{} Action: {}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].health, enemys[i].stamina, enemys[i].action))

def displayStats(player,enemys):
    os.system('clear')
    for i in range(0,len(enemys)):
        print('''
        {} {}: Damage Range:{}-{} Stamina:{} Max Stamina:{}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].guessLowDamage(), enemys[i].guessHighDamage(), enemys[i].stamina, enemys[i].max_stamina))
    time.sleep(3)
