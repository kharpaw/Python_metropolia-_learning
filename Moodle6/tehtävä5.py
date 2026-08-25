'''
Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise the same
as the original list except that all uneven numbers have been removed.
For testing, write a main program where you create a list, call the function,
and then print out both the original as well as the cut-down list.
'''

def interger(number):
    result = []
    for i in number:
        if i % 2 == 0:
            result.append(i)
    return result
        


def main():
    numbers = [1,2,3,4,5,6,7,8]
    
    print(numbers)
    print(interger(numbers))
         
main()