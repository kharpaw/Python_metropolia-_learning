import math

def diameter(centimeter, euro):
    radius = centimeter / 2
    area = math.pi * radius ** 2
    area_m2 = area / 10000
    return euro / area_m2


def main():
    user1 = float(input("Enter the diameter of the first pizza: "))
    price1 = float(input("Enter the price of the first pizza: "))

    user2 = float(input("Enter the diameter of the second pizza: "))
    price2 = float(input("Enter the price of the second pizza: "))

    price_first = diameter(user1, price1)
    price_second = diameter(user2, price2)

    if price_first < price_second:
        print("Pizza 1 provides better value for money.")
    elif price_first < price_second:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


main()