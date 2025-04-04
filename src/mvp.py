def calculo(kills,assists,deaths):
    return kills * 3 + assists - deaths
    
def actualizar(stats,ronda):
    mvp = None
    max = -999

    for jugador, datos in ronda.items():
        kills = datos['kills']
        deaths = datos['deaths']
        assists = datos['assists']
        puntos = calculo(kills,assists,deaths)

        if jugador not in stats:
            stats[jugador] = {'puntos': 0, 'kills': 0, 'deaths': 0, 'assists': 0, 'mvp': 0}
        stats[jugador]['puntos'] += puntos
        stats[jugador]['kills'] += kills
        stats[jugador]['deaths'] += deaths
        stats[jugador]['assists'] += assists

        if puntos > max:
            max = puntos
            mvp = jugador
        
        if mvp: 
            stats[jugador]['mvp'] += 1
        
        return mvp, max

def imprimir(stats):
    print(f"{'Jugador':<10} {'Kills':<6} {'Assists':<8} {'Muertes':<8} {'MVPs':<5} {'Puntos':<6}")
    print("-" * 50)
    for jugador, datos in sorted(stats.items(), key=lambda x: x[1]['puntos'], reverse=True):
        print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<8} {datos['deaths']:<8} {datos['mvp']:<5} {datos['puntos']:<6}")
