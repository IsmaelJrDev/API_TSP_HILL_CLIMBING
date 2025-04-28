from flask import Flask, request, jsonify
from hillClimbing import hill_climbing, evalua_ruta

app = Flask(__name__)

@app.route('/tsp', methods=['POST'])
def tsp():
    data = request.json
    coord = data.get('coord', {})
    
    if not coord:
        return jsonify({"error": "No se proporcionaron coordenadas"}), 400

    # Ejecutar el algoritmo Hill Climbing
    ruta = hill_climbing(coord)
    distancia_total = evalua_ruta(ruta, coord)

    return jsonify({
        "ruta_optima": ruta,
        "distancia_total": round(distancia_total, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)