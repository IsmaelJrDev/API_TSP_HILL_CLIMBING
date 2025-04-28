import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    ciudad1 = ruta[-1]
    ciudad2 = ruta[0]
    total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def hill_climbing(coord, ciudad_origen):
    # Crear la ruta inicial aleatoria
    ruta = list(coord.keys())
    ruta.remove(ciudad_origen)
    random.shuffle(ruta)
    ruta.insert(0, ciudad_origen)  # Asegurar que la ciudad de origen sea la primera

    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta, coord)
        for i in range(1, len(ruta)):  # No intercambiar la ciudad de origen
            if mejora:
                break
            for j in range(1, len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    dist = evalua_ruta(ruta_tmp, coord)
                    if dist < dist_actual:
                        mejora = True
                        ruta = ruta_tmp[:]
                        break
    return ruta