from random import randint

def checkEnemyAction(player, enemys):
    for i in range(0,len(enemys)):
        randNum = randint(0,1)
        
        if enemys[i].stamina <= 0: # Check if out of stamina
            randNum = 1
        
        if randNum == 0: # Attack
            enemys[i].stamina -= 5
            damageDealt = enemys[i].calcDamage() #Calculate amount of damage taken
            enemys[i].action = 'Attacked Player for {} Damage'.format(damageDealt)
            player.health -= damageDealt
        
        if randNum == 1: # Wait
            enemys[i].stamina += 5
            
