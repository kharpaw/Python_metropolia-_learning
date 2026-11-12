from flask import Flask, request, Response
import json
import mysql.connector


app = Flask(__name__)

#DB connection
def mysql_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "pawan",
            database = "flight_game"
        )
        return connection

    except mysql.connector.Error as error:
        print("Database connection failed")
        print(error)
        mysql_connection()

#Get icoa
def get_airport(icoa):
    connection = mysql_connection()
    cursor = connection.cursor()
    sql = "SELECT ident, name, municipality from AIRPORT where ident = %s"
    cursor.execute(sql, (icoa,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result
    
@app.route("/airport/<icoa>")
def icoa(icoa):
    try:
        ode = icoa.upper()
        row = get_airport(icoa)
    
        status_code = 200
        vastaus= {
        "Status_code": status_code,
        "ICOA": row[0],
        "Name": row[1],
        "Location":row[2]
    }
        return vastaus

    except ValueError:
        status_code = 400
        vastaus = {
            "status": status_code,
            "teksti":"Virhellinen yhteenlaskettava"
        }
        jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)        
    
    
    
    
        


    





