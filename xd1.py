import re

def validar_nombre(nombre):
    expnom = r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$"
    if re.match(expnom, nombre):
        return True
    else:
        return False

def solicitar_nombre():
    while True:
        nombre = input("Por favor, ingresa tu nombre: ")
        if validar_nombre(nombre):
            print("Nombre válido.")
            return nombre
        else:
            print("Nombre inválido. Inténtalo de nuevo.")

# Llamar a la función para solicitar el nombre
nombre = solicitar_nombre()