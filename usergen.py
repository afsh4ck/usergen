import os
import datetime
import itertools

# Definir variables de color
AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def cabecera():
    clear_screen()
    print(ROJO + title + RESET)
    print(divider)

title = """
██╗   ██╗███████╗███████╗██████╗  ██████╗ ███████╗███╗   ██╗
██║   ██║██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝████╗  ██║
██║   ██║███████╗█████╗  ██████╔╝██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║╚════██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝███████║███████╗██║  ██║╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝                                                   
Username List Generator                          < afsh4ck >"""

divider = """------------------------------------------------------------
"""

def generar_nombres_usuario(nombre, apellidos):
    nombres_usuario = set()
    nombre = nombre.lower().replace(" ", "")  # Eliminar espacios entre palabras del nombre
    apellidos = apellidos.lower().replace(" ", "")  # Eliminar espacios entre palabras del apellido

    # Obtener el año actual
    año_actual = datetime.datetime.now().year

    # Combinar nombre, apellidos y el año actual y variantes de hasta 50 años menos sin separadores
    for num in range(51):
        año = año_actual - num
        nombres_usuario.add(nombre + apellidos)
        nombres_usuario.add(nombre + str(año) + apellidos)
        nombres_usuario.add(str(año) + nombre + apellidos)
        nombres_usuario.add(apellidos + nombre)
        nombres_usuario.add(apellidos + str(año) + nombre)
        nombres_usuario.add(str(año) + apellidos + nombre)

    # Agregar nuevas variantes reemplazando el nombre por la primera letra del nombre y el apellido por la primera letra del apellido
    primera_letra_nombre = nombre[0]
    primera_letra_apellidos = apellidos[0]
    nombres_usuario.add(primera_letra_nombre + apellidos)
    nombres_usuario.add(apellidos + primera_letra_nombre)
    nombres_usuario.add(primera_letra_nombre + apellidos + str(año))
    nombres_usuario.add(apellidos + primera_letra_nombre + str(año))
    nombres_usuario.add(primera_letra_nombre + str(año) + apellidos)
    nombres_usuario.add(primera_letra_apellidos + nombre)
    nombres_usuario.add(nombre + primera_letra_apellidos)
    nombres_usuario.add(primera_letra_apellidos + nombre + str(año))
    nombres_usuario.add(nombre + primera_letra_apellidos + str(año))
    nombres_usuario.add(primera_letra_apellidos + str(año) + nombre)

    # Combinar nombre y apellidos con puntos, guiones y guiones bajos, y el año actual y variantes de hasta 50 años menos
    separadores = ['.', '-', '_']
    for separador in separadores:
        for num in range(51):
            año = año_actual - num
            nombres_usuario.add(nombre + separador + apellidos)
            nombres_usuario.add(nombre + separador + str(año) + separador + apellidos)
            nombres_usuario.add(str(año) + separador + nombre + separador + apellidos)
            nombres_usuario.add(apellidos + separador + nombre + separador + str(año))
            nombres_usuario.add(apellidos + separador + str(año) + separador + nombre)
            nombres_usuario.add(nombre + separador + str(año) + separador + apellidos)
            nombres_usuario.add(apellidos + separador + str(año) + separador + nombre)
            nombres_usuario.add(primera_letra_nombre + separador + apellidos)
            nombres_usuario.add(primera_letra_nombre + separador + str(año) + separador + apellidos)
            nombres_usuario.add(str(año) + separador + primera_letra_nombre + separador + apellidos)
            nombres_usuario.add(apellidos + separador + primera_letra_nombre + separador + str(año))
            nombres_usuario.add(apellidos + separador + str(año) + separador + primera_letra_nombre)
            nombres_usuario.add(primera_letra_apellidos + separador + nombre)
            nombres_usuario.add(primera_letra_apellidos + separador + str(año) + separador + nombre)
            nombres_usuario.add(str(año) + separador + primera_letra_apellidos + separador + nombre)
            nombres_usuario.add(nombre + separador + primera_letra_apellidos + separador + str(año))
            nombres_usuario.add(nombre + separador + str(año) + separador + primera_letra_apellidos)
            nombres_usuario.add(primera_letra_apellidos + separador + str(año) + separador + nombre)
            nombres_usuario.add(nombre + separador + str(año) + separador + primera_letra_apellidos)

    return nombres_usuario

def exportar_nombres_usuario(nombres_usuario, archivo):
    with open(archivo, "w") as file:
        for username in nombres_usuario:
            file.write(username + "\n")
    print(f"\nLos nombres de usuario se han exportado exitosamente a '{archivo}'.")

while True:
    cabecera()

    # Pedir al usuario que ingrese su nombre y apellidos
    nombre = input(VERDE + "[+] Introduce un nombre: " + RESET)
    apellidos = input(VERDE + "[+] Introduce apellidos o palabras clave (separados por espacios): " + RESET)

    # Generar los nombres de usuario
    nombres_usuario = generar_nombres_usuario(nombre, apellidos)

    # Mostrar los nombres de usuario generados
    print("\nNombres de usuario generados:")
    for username in nombres_usuario:
        print(username)

    # Pedir al usuario si desea exportar los nombres de usuario a un archivo de texto
    exportar = input(VERDE + "\n[+] ¿Deseas exportar el listado a un archivo de texto? (s/n): " + RESET)
    if exportar.lower() == "s":
        archivo = input(VERDE + "[+] Ingresa el nombre del archivo (incluyendo la extensión .txt): " + RESET)
        exportar_nombres_usuario(nombres_usuario, archivo)

    # Pedir al usuario si desea volver a empezar el proceso
    reiniciar = input(VERDE + "\n[+] ¿Deseas generar más nombres de usuario? (s/n): " + RESET)
    if reiniciar.lower() != "s":
        print(ROJO + "\n[+] Happy Hacking ;)" + RESET)
        break
