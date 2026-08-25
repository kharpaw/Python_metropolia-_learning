'''
Write a program that asks the user for a number of a month and
then prints out the corresponding season (spring, summer, autumn, winter).
Save the seasons as strings into a tuple in your program. We can define
each season to last three months, December being the first month of winter.
'''

user = int(input("Enter the month number (1-12): "))

if user == 0 or user <  0:
    print("This month doesnot exist")
    exit()

year_of_the_seasons = ("spring", "summer", "autumn", "winter")

season = year_of_the_seasons[(user -1) // 3]

print(season)



