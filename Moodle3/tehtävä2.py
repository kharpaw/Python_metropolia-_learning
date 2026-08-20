'''
2. Write a program that asks the user to enter the cabin
class of a cruise ship and then prints out a written description according to the list below.
You must use an if/elif/else structure in your solution.

LUX: upper-deck cabin with a balcony.
A: above the car deck, equipped with a window.
B: windowless cabin above the car deck.
C: windowless cabin below the car deck.
If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.


'''

user = input("Enter the cabin clas of a cruise ship (LUX, A, B,C): ")

if user == "LUX":
    print("upper-deck cabin with a balcony.")
elif user == "A":
    print("above the car deck, equipped with a window.")
elif user == "B":
    print("windowless cabin above the car deck.")
elif user == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")