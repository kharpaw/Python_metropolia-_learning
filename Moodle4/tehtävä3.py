'''
3. Write a program that asks the user to enter numbers until
they enter an empty string to quit. Finally, the program prints
out the smallest and largest number from the numbers it received.
'''

numbers = []

while True:
    user = input("Enter a number (Enter to quit): ")

    if user == "":
        break

    numbers.extend(map(int, user.split()))
    # List will convert something into python list
    #Map applies function to every items and make it into integrate
    #split methods seperates the text

    if numbers:
        print(f"Smallest: {min(numbers)}")
        print(f"Largest: {max(numbers)}")