'''
Write a function that gets a list of integers as a parameter.
The function returns the sum of all the numbers in the list.
For testing, write a main program where you create a list,
call the function, and print out the value it returned.
'''

def integers(numbers):
    return sum(numbers)

def main():
    numbers = [1, 2, 3, 4, 5]

    result = integers(numbers)
    print(result)

main()