from flask import Flask, request, jsonify, render_template
from hillClimbing import hill_climbing, evalua_ruta

app = Flask(__name__)

# Coordenadas de las ciudades
COORD = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hill_climbing', methods=['POST'])
def api_hill_climbing():
    data = request.json
    ciudad_origen = data.get('ciudad_origen')

    if ciudad_origen not in COORD:
        return jsonify({'error': 'Ciudad de origen no válida'}), 400

    ruta_optima = hill_climbing(COORD, ciudad_origen)
    distancia_total = evalua_ruta(ruta_optima, COORD)

    # Agregar la ciudad de origen al final de la ruta para cerrar el ciclo
    ruta_optima.append(ciudad_origen)

    return jsonify({
        'ruta_optima': ruta_optima,
        'distancia_total': distancia_total
    })

if __name__ == '__main__':
    app.run(debug=True)