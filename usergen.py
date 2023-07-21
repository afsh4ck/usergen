import itertools
import os

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

# Mostrar cabecera
cabecera()
def generate_initial_variants(name):
    variants = []
    first_letter = name[0].lower()
    variants.append(first_letter)
    return variants

def generate_date_variants(name, first_lastname, second_lastname, birth_years, current_years):
    variants = []
    for birth_year in birth_years:
        if birth_year not in name and birth_year not in first_lastname and birth_year not in second_lastname:
            variants.append(name + birth_year)
            variants.append(name + first_lastname + birth_year)
            variants.append(name + first_lastname + second_lastname + birth_year)
            variants.append(name + "." + birth_year)
            variants.append(name + "." + first_lastname + "." + birth_year)
            variants.append(name + "." + first_lastname + "." + second_lastname + "." + birth_year)
            variants.append(name + "_" + birth_year)
            variants.append(name + "_" + first_lastname + "_" + birth_year)
            variants.append(name + "_" + first_lastname + "_" + second_lastname + "_" + birth_year)
            variants.append(name + "-" + birth_year)
            variants.append(name + "-" + first_lastname + "-" + birth_year)
            variants.append(name + "-" + first_lastname + "-" + second_lastname + "-" + birth_year)
            for current_year in current_years:
                if current_year not in name and current_year not in first_lastname and current_year not in second_lastname and current_year != birth_year:
                    variants.append(name + current_year)
                    variants.append(name + first_lastname + current_year)
                    variants.append(name + first_lastname + second_lastname + current_year)
                    variants.append(name + "." + current_year)
                    variants.append(name + "." + first_lastname + "." + current_year)
                    variants.append(
                        name + "." + first_lastname + "." + second_lastname + "." + current_year)
                    variants.append(name + "_" + current_year)
                    variants.append(name + "_" + first_lastname + "_" + current_year)
                    variants.append(
                        name + "_" + first_lastname + "_" + second_lastname + "_" + current_year)
                    variants.append(name + "-" + current_year)
                    variants.append(name + "-" + first_lastname + "-" + current_year)
                    variants.append(
                        name + "-" + first_lastname + "-" + second_lastname + "-" + current_year)
    return variants

def check_initial_variants_availability(variants_list, name, first_lastname, second_lastname):
    filtered_variants = []
    for variant in variants_list:
        if name[0].lower() in variant and first_lastname[0].lower() in variant and second_lastname[0].lower() in variant:
            continue
        filtered_variants.append(variant)
    return filtered_variants

def generate_usernames(target_name, first_lastname, second_lastname, birth_year, current_year):
    # Eliminar espacios en blanco del nombre y apellidos
    target_name = target_name.replace(" ", "")
    first_lastname = first_lastname.replace(" ", "")
    second_lastname = second_lastname.replace(" ", "")

    # Obtener los últimos 2 dígitos del año de nacimiento
    birth_year_2digits = birth_year[-2:]

    # Obtener los últimos 2 dígitos del año actual
    current_year_2digits = current_year[-2:]

    # Combinar el nombre, apellidos, año de nacimiento y año actual para obtener posibles nombres de usuario
    names = [
        target_name.lower(),
        target_name[0].lower() + first_lastname[0].lower() + second_lastname[0].lower()
    ]

    first_lastnames = [
        first_lastname.lower(),
        first_lastname[0].lower() + second_lastname[0].lower() + target_name[0].lower()
    ]

    second_lastnames = [
        second_lastname.lower(),
        second_lastname[0].lower() + first_lastname[0].lower() + target_name[0].lower()
    ]

    birth_years = [
        birth_year,
        birth_year_2digits
    ]

    current_years = [
        current_year,
        current_year_2digits
    ]

    usernames = []
    for name in names:
        for first_lastname in first_lastnames:
            for second_lastname in second_lastnames:
                if name != "" and first_lastname != "" and second_lastname != "":
                    # Agregar variantes con el nombre, 1er apellido y 2º apellido
                    usernames.append(name + first_lastname)
                    usernames.append(name + first_lastname + second_lastname)
                    usernames.append(name + "." + first_lastname)
                    usernames.append(name + "." + first_lastname + "." + second_lastname)
                    usernames.append(name + "_" + first_lastname)
                    usernames.append(name + "_" + first_lastname + "_" + second_lastname)
                    usernames.append(name + "-" + first_lastname)
                    usernames.append(name + "-" + first_lastname + "-" + second_lastname)

                    # Agregar variantes con la primera letra del nombre, 1er apellido y 2º apellido
                    usernames.extend(generate_initial_variants(name) + generate_initial_variants(first_lastname) + generate_initial_variants(second_lastname))

                    # Agregar nuevas variantes con los apellidos y el nombre en diferentes órdenes
                    usernames.append(first_lastname + second_lastname + name)
                    usernames.append(first_lastname + name)
                    usernames.append(second_lastname + name)

                    # Agregar más combinaciones según tus necesidades
                    # Por ejemplo:
                    usernames.append(name + second_lastname + first_lastname)
                    usernames.append(first_lastname + birth_year)
                    usernames.append(second_lastname + birth_year)
                    usernames.append(first_lastname + second_lastname + birth_year)

                    # Agregar variantes con el nombre, 1er apellido , 2º apellido y fechas
                    variants_list = generate_date_variants(name, first_lastname, second_lastname, birth_years, current_years)

                    # Eliminar variantes que incluyan la primera letra del nombre, 1er apellido y 2º apellido
                    filtered_variants = check_initial_variants_availability(variants_list, name, first_lastname, second_lastname)

                    usernames.extend(filtered_variants)

    return usernames

def main():
    while True:
        print(CYAN + "==================================================" + RESET)
        print(CYAN + "[+] Bienvenido al generador de nombres de usuario." + RESET)
        print(CYAN + "==================================================" + RESET)
        print("\n")

        try:
            target_name = input(VERDE + "[+] Introduce el nombre del objetivo: " + RESET)
            first_lastname = input(VERDE + "[+] Introduce el primer apellido del objetivo: " + RESET)
            second_lastname = input(VERDE + "[+] Introduce el segundo apellido del objetivo: " + RESET)
            birth_year = input(VERDE + "[+] Introduce el año de nacimiento del objetivo: " + RESET)
            current_year = input(VERDE + "[+] Introduce el año actual: " + RESET)

            usernames = generate_usernames(target_name, first_lastname, second_lastname, birth_year, current_year)

            print(AMARILLO + "\n[*] Creando listado de posibles nombres de usuario..." + RESET)

            # Eliminar duplicados de la lista de nombres de usuario
            usernames = list(set(usernames))

            print(VERDE + "\n[+] Lista de posibles nombres de usuario relacionados con el objetivo:" + RESET)
            for username in usernames:
                print(username)

            export_choice = input(ROJO + "\n[!] ¿Deseas exportar el listado en un archivo de texto? (s/n): " + RESET).lower()
            if export_choice == "s":
                filename = input("[+] Introduce el nombre del archivo para guardar el listado (sin extensión): ")
                with open(f"{filename}.txt", "w") as file:
                    for username in usernames:
                        file.write(f"{username}\n")
                print(VERDE + "[+] El listado de nombres de usuario se ha guardado en el archivo {}.txt".format(filename))

        except KeyboardInterrupt:
            exit_choice = input(ROJO + "\n[!] ¿Deseas salir del programa? (s/n): " + RESET).lower()
            if exit_choice == "s":
                print(VERDE + "[+] Happy hacking ;)" + RESET)
                break
            elif exit_choice == "n":
                continue
            else:
                print(ROJO + "[!] Opción inválida. Por favor, selecciona 's' para salir o 'n' para continuar." + RESET)

        input("\n[*] Presiona Enter para continuar...")
        cabecera()

if __name__ == "__main__":
    main()
