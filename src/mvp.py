# mvp.py
def calcular_puntaje(estadisticas):
    return estadisticas["kills"] * 3 + estadisticas["assists"] * 1 - estadisticas["deaths"] * 1

def procesar_rondas(rondas):
    progreso = {}
    for i, ronda in enumerate(rondas, 1):
        print(f"--- Ronda {i} ---")
        puntajes_ronda = {}
        for jugador, datos in ronda.items():
            puntajes_ronda[jugador] = calcular_puntaje(datos) 

        max_puntaje = max(puntajes_ronda.values())  
        mvp_ronda = [j for j, p in puntajes_ronda.items() if p == max_puntaje]  

        print(f"MVP(s) de la ronda: {', '.join(mvp_ronda)}")

        for jugador, datos in ronda.items():
            if jugador not in progreso:
                progreso[jugador] = {"kills": 0, "assists": 0, "deaths": 0, "mvps": 0, "puntos": 0}

            progreso[jugador]["kills"] += datos["kills"]
            progreso[jugador]["assists"] += datos["assists"]
            progreso[jugador]["deaths"] += int(datos["deaths"])
            progreso[jugador]["puntos"] += puntajes_ronda[jugador]  

            if jugador in mvp_ronda:
                progreso[jugador]["mvps"] += 1  
    
        imprimir_tabla(progreso)
        print("\n")

    return progreso

def imprimir_tabla(progreso):
    ordenado = sorted(progreso.items(), key=lambda x: x[1]["puntos"], reverse=True)
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<11} {'Muertes':<8} {'MVPs':<5} {'Puntos':<6}")
    print("-" * 56)
    for jugador, stats in ordenado:
        print(f"{jugador:<10} {stats['kills']:<6} {stats['assists']:<11} {stats['deaths']:<8} {stats['mvps']:<5} {stats['puntos']:<6}")
