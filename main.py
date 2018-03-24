#!/usr/bin/python3
import function, menu, classes

from random import randint

print('Welcome to the DANGERZONE!')
player = menu.choosePlayer()
enemys = function.randEnemy(randint(1,2))

menu.mainLoop(player,enemys) # Starts the main loop for the game
