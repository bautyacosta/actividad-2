def validar(nombre):
    if len(nombre) <5:
        return "el nombre debe tener al menos 5 caracteres"
    if not any(caracter.isdigit() for caracter in nombre):
        return "el nombre debe contener al menos un número"
    if not any(caracter.isupper() for caracter in nombre):
        return "el nombre debe contener al menos una letra mayúscula"
    if not nombre.isalnum():
        return "el nombre solo puede contener letras y números"
    return "nombre válido"