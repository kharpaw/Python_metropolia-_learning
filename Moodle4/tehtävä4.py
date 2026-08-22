'''
Write a game where the computer draws a random integer between 1 and 10.
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
Notice that the computer must not change the number between guesses.
'''

import random

lowest_number = 1
highest_number = 10
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python Number Guessing game")
print(f"Select a number between {lowest_number} and {highest_number}")

while is_running:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
    
        if guess < lowest_number or guess > highest_number:
            print("That number is out of range")
            print(f"Select a number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print(f"Correct! The answer was {answer} ")
            print(f"Total guesses: {guesses}")
            is_running = False
        
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_number} and {highest_number}")
        