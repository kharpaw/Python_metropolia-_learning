'''
Write a function that gets the quantity of gasoline in American gallons
and returns the number converted to litres. Write a main program that
asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue until
the user inputs a negative value.
'''

def gallons_to_litres(gallons):
    return gallons * 3.785

def main():
    while True:
        user = int(input("Enter the gallons to converts the value to liers: "))
    
        if user < 0:
            print("Negative value does not process the program.")
            break
        
        result = gallons_to_litres(user)
        print(f"After converting result is {result} litres.")
        
main()