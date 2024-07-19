import geopy.distance

def obtener_distancia(ciudad_inicio, ciudad_final, ubicaciones):
    return geopy.distance.distance(ubicaciones[ciudad_inicio], ubicaciones[ciudad_final]).km

ubicaciones = {
    'Santiago': (-33.4489, -70.6693),
    'Buenos Aires': (-34.6037, -58.3816),
    'Mendoza': (-32.8894, -68.8458),
    'Valparaiso': (-33.0472, -71.6127)
}

while True:
    ciudad_origen = input("Indica la ciudad de origen (o 's' para salir): ").strip()
    if ciudad_origen.lower() == 's':
        break

    ciudad_destino = input("Indica la ciudad de destino: ").strip()

    if ciudad_origen not in ubicaciones or ciudad_destino not in ubicaciones:
        print("Ciudad no reconocida, por favor intenta de nuevo.")
        continue

    distancia_km = obtener_distancia(ciudad_origen, ciudad_destino, ubicaciones)
    distancia_millas = distancia_km * 0.621371

    print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia_km:.2f} km o {distancia_millas:.2f} millas.")

    tipo_transporte = input("Indica el medio de transporte (auto, avión, bicicleta): ").strip().lower()

    if tipo_transporte == "auto":
        tiempo_estimado = distancia_km / 100
    elif tipo_transporte == "avion":
        tiempo_estimado = distancia_km / 800 
    elif tipo_transporte == "bicicleta":
        tiempo_estimado = distancia_km / 20
    else:
        print("Tipo de transporte no reconocido.")
        continue

    print(f"El tiempo estimado de viaje en {tipo_transporte} es de {tiempo_estimado:.2f} horas.")
    print(f"Desde {ciudad_origen} hasta {ciudad_destino}, viajando en {tipo_transporte}, tomaría aproximadamente {tiempo_estimado:.2f} horas.")

