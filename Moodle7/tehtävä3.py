airports = {}

while True:
    print("1. Enter a new airport: ")
    print("2. Fetch the information: ")
    print("3. Quit")

    user = int(input("Choose the option: "))

    if user == 1:
        icao = input("Enter the ICAO code: ")
        airport = input("Enter the name of airport: ")

        airports[icao] = airport

    elif user == 2:
        code = input("Enter the ICAO code: ")

        if code in airports:
            print(airports[code])
        else:
            print("Airport not found.")

    elif user == 3:
        print("bye")
        break

    else:
        print("Invalid option")

