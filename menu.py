import os,sys, function, AI

def mainLoop(player,enemys):
    
    while True:
        try:
            os.system('clear')
            print("You face {} enemys".format(len(enemys)))
            printEnemys(enemys)
            print("{}: Stamina:{} Health:{} Last Action: {}".format(player.name, player.stamina, player.health, player.action))
            print("")
           
            action = input('1.Attack 2.Wait 9.Run Away --> ')
            function.checkPlayerAction(player, enemys, action)
            AI.checkEnemyAction(player, enemys)
            function.checkPlayerHealth(player)
            function.checkEnemyHealth(enemys)
            function.winCondition(enemys)
        except Exception as e:
            pass

def printEnemys(enemys):
    for i in range(0,len(enemys)):
        print('''
        {} {}: Health:{} Stamina:{} Action: {}
        '''.format(str(i + 1) + ':', enemys[i].name, enemys[i].health, enemys[i].stamina, enemys[i].action))
