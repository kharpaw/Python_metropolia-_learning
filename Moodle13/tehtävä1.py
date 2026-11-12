from flask import Flask, request, Response
import json
app= Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n ** 0.5)+ 1):
            if n % i == 0:
                return False
        return True
        
@app.route("/number/<primenumber>")
def primenumber(primenumber):
    try:
        num = int(primenumber)
        status_code = 200
        vastaus = {
            "status":status_code,
            "is_prime": is_prime(num)
        }
        return vastaus
    
    
    except ValueError:
        tilakoodi = 400
        vastaus = {
        "status": tilakoodi,
        "teksti": "Virheellinen yhteenlaskettava"
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