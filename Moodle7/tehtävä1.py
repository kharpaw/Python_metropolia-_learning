'''
Write a program that asks the user for a number of a month and
then prints out the corresponding season (spring, summer, autumn, winter).
Save the seasons as strings into a tuple in your program. We can define
each season to last three months, December being the first month of winter.
'''

user = int(input("Enter the month number (1-12): "))

if user < 0 or user > 12:
    print("Invalid month")
    exit()

seasons = ("spring", "summer", "autumn", "winter")

months = {
        1: 3,
        2: 3,
        3: 0,
        4: 0,
        5: 0,
        6: 1,
        7: 1,
        8: 1,
        9: 2,
        10: 2,
        11: 2,
        12: 3
}

season = seasons[months[user]]

print(season)



