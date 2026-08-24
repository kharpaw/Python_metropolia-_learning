'''
Modify the function above so that it gets the number of sides
on the dice as a parameter. With the modified function you can
for example roll a 21-sided role-playing dice. The difference to the
last exercise is that the dice rolling in the main program continues
until the program gets the maximum number on the dice, which is asked
from the user at the beginning.
'''

import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides: "))

while True:
    result = roll_dice(sides)
    print(result)
    
    if result == sides:
        break
    
