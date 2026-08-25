import random

user = int(input("How many random points should be generated? "))

n = 0
i = 0

while i < user:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

        i += 1

        pi = 4 * n / user

        print("Approximation of pi:", pi)