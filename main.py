#!/usr/bin/python3
import function, menu, classes

from random import randint

print('Welcome to the DANGERZONE!')
player = classes.Player(input('Please enter your name: '))
enemys = function.randEnemy(randint(1,2))

menu.mainLoop(player,enemys)
