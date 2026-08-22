'''
1. Write a program that asks the user how many dice to roll.
The program rolls all the dice once and prints out the sum of the numbers.
Use a for loop.
'''

import random 

total = 0
dice = int(input("How many dice you want to roll: "))

for i in range(dice):
    roll = random.randint(1, 6)
    total += roll
    
print(f"The total sum of the dice {total}")