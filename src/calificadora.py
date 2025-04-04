def calificar(ms):
    ms = int(ms)
    if ms < 200: 
        return "rapido"
    if ms >= 200 and ms < 500:
        return "normal"
    if ms >= 500:
        return "lento"