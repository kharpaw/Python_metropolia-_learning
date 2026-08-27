"""
Write a program that asks the user to enter the ICAO code of an airport.
The program fetches and prints out the corresponding airport name and location
(town) from the airport database used on this course. The ICAO codes are stored
in the ident column of the airport table.
"""
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pawan",
        database="flight_game"
    )

    print("Database connected successfully ✅")
    cursor = conn.cursor()

    icao = input("Enter the ICAO code of an airport: ")

    cursor.execute(
        "SELECT name, municipality FROM airport WHERE ident = %s",
        (icao,)
    )

    result = cursor.fetchone()

    if result:
        print("Airport:", result[0])
        print("Location:", result[1])
    else:
        print("Airport not found")

        cursor.close()
        conn.close()

except mysql.connector.Error as e:
    print("Database error:")
    print(e)