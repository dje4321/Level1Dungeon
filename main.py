import function, menu, classes

from random import randint

print('Welcome to the DANGERZONE!')
#player = classes.Player(input('Please enter your name: '))
player = classes.Player('Emily')
enemys = function.randEnemy(3)

# Test Values
player.health = 1000
player.stamina = 5

menu.mainLoop(player,enemys)
