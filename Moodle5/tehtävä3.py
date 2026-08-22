'''
Write a program that asks the user for an integer and
tells if the number is a prime number. Prime numbers are number
that are only divisible by one or the number itself.

For example, 13 is a prime number as it can only be divided
by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
'''

number = int(input("Enter the number you want to check: "))


if number < 2:
    print(f"{number} is not prime number.")
    exit()

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime number and it is divisible by {i}.")
        exit()

print(f"{number} is a prime number and it is only divided by 1 and itself.")