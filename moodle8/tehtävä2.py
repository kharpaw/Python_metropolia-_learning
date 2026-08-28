'''
2. Write a program that asks the user to enter the area code (for example FI)
and prints out the airports located in that country ordered by airport type.
For example, Finland has 65 small airports, 15 helicopter airports and so on.
'''
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

    country_code = input(
        "Enter the area code (for example FI): "
    ).upper()

    cursor.execute(
        """
        SELECT type, COUNT(*)
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
        ORDER BY type
        """,
        (country_code,)
    )

    result = cursor.fetchall()

    if result:
        print(f"\nAirports in {country_code}:")

        for airport_type, count in result:
            print(f"{airport_type}: {count}")

    else:
        print("No airports found for that country.")

        cursor.close()
        conn.close()

except mysql.connector.Error as e:
    print("Database error:")
    print(e)