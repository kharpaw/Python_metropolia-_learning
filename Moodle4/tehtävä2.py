'''
Write a program that converts inches to centimeters
until the user inputs a negative value. Then the program ends.
'''

while True:
    user = int(input("Enter the number(inches to centimeter): "))
    
    if user < 0:
        break
    
    cm = user * 2.54
    print(f"{user} inch to centermeter is {cm}cm.")
    

