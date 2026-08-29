'''
Write a program that asks the user to enter the ICAO codes of two airports.
The program prints out the distance between the two airports in kilometers.
The calculation is based on the airport coordinates fetched from the database.
Calculate the distance using the geopy library:
https://geopy.readthedocs.io/en/stable/.
Install the library by selecting View /
Tool Windows / Python Packages in your PyCharm IDE,
write geopy into the search field and finish the installation.
'''
import mysql.connector
from geopy.distance import geodesic

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pawan",
        database="flight_game"
    )

    print("MariaDB connected successfully")

    cursor = conn.cursor()

    user1 = input("Enter the first airport ICAO code: ").upper()
    user2 = input("Enter the second airport ICAO code: ").upper()

    cursor.execute("""
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
    """, (user1,))

    airport1 = cursor.fetchone()

    cursor.execute("""
    SELECT latitude_deg, longitude_deg
    FROM airport
    WHERE ident = %s
    """, (user2,))

    airport2 = cursor.fetchone()

    if airport1 and airport2:

        coordinates1 = (airport1[0], airport1[1])
        coordinates2 = (airport2[0], airport2[1])

        distance = geodesic(coordinates1, coordinates2).kilometers

        print(f"Distance between {user1} and {user2}: {distance:.2f} km")

    else:
        print("Airports were not found.")

        cursor.close()
        conn.close()

except mysql.connector.Error as e:
    print("Database error:")
    print(e)