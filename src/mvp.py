def calcular_puntaje(kills, assists, deaths):
    puntos = kills * 2 + assists
    if deaths:
        puntos -= 1
    return puntos

def procesar_rondas(rondas):
    estadisticas = {}

    for i, ronda in enumerate(rondas, 1):
        print(f"\n--- RONDA {i} ---")
        mvp = None
        max_puntaje = float('-inf')

        for jugador, datos in ronda.items():
            if jugador not in estadisticas:
                estadisticas[jugador] = {
                    'kills': 0,
                    'assists': 0,
                    'deaths': 0,
                    'MVPs': 0,
                    'puntos': 0
                }

            kills = datos['kills']
            assists = datos['assists']
            deaths = 1 if datos['deaths'] else 0

            puntaje = calcular_puntaje(kills, assists, deaths)

            estadisticas[jugador]['kills'] += kills
            estadisticas[jugador]['assists'] += assists
            estadisticas[jugador]['deaths'] += deaths
            estadisticas[jugador]['puntos'] += puntaje

            if puntaje > max_puntaje:
                max_puntaje = puntaje
                mvp = jugador
                
        estadisticas[mvp]['MVPs'] += 1
        print(f"MVP de la ronda: {mvp}")

        print("\nJugador     Kills  Assists  Deaths  MVPs  Puntos")
        print("--------------------------------------------------")
        for jugador, datos in sorted(estadisticas.items(), key=lambda x: x[1]['puntos'], reverse=True):
            print(f"{jugador:<12}{datos['kills']:>5}  {datos['assists']:>7}  {datos['deaths']:>6}  {datos['MVPs']:>4}  {datos['puntos']:>7}")
