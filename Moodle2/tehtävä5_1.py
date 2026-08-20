#1.Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

import random

#This generate random digit betwee 0 and 0
code3 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)

#This generate random digit between 1 and 6
code4 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)

print("3-digit code:", code3)
print("4-digit code:", code4)


