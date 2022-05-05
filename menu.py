from colorama import init, Fore
import pyodbc
import time
import os

def clear():
    os.system("cls")

init(autoreset= True)

def validation(msg, a, b):
    while True:
        clear()
        try:
            logo()
            print("\n" + msg + "\n")
            opc = int(input("Ingrese una opcion: "))
            if opc >= a and opc <= b:
                return opc
            else:
                clear()
                print(Fore.RED + "[ X ] Oops!, Opcion invalida... Intente de nuevo.")
                time.sleep(2)
                clear()

        except ValueError:
            clear()
            print(Fore.RED + "[ X ] Oops!, Opcion invalida... Intente de nuevo.")
            time.sleep(2)
            clear()

def logo():
    print("\t\t" + "#"*65, end="\n\t\t#" + " "*63 + "#\n")
    print("\t\t#\t" + Fore.RED             + " /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.BLUE            + "| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.YELLOW          + "| $$  | $$| $$  \ $$| $$$$| $$| $$  \ $$| $$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.MAGENTA         + "| $$  | $$| $$$$$$$$| $$ $$ $$| $$$$$$$$| $$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.CYAN            + "| $$  | $$| $$__  $$| $$  $$$$| $$__  $$| $$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.GREEN           + "| $$  | $$| $$  | $$| $$\  $$$| $$  | $$| $$       " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.WHITE           + "|  $$$$$$/| $$  | $$| $$ \  $$| $$  | $$| $$$$$$$$ " + Fore.RESET +"\t#")
    print("\t\t#\t" + Fore.LIGHTMAGENTA_EX + " \______/ |__/  |__/|__/  \__/|__/  |__/|________/ " + Fore.RESET +"\t#", end="\n\t\t#" + " "*63 + "#\n")
    print("\t\t" + "#"*65)


def menu():
    msg = "[ 1 ] Crear\n[ 2 ] Mostrar\n[ 3 ] Modificar\n[ 4 ] Eliminar\n[ 5 ] Salir"

    opc = validation(msg, 1, 5)

    if opc == 1:
        crear()
    elif opc == 2:
        mostrar()
    elif opc == 3:
        modificar()
    elif opc == 4:
        eliminar()
    else:
        exit()

    return opc


def crear(cursor):
    msg = "[ 1 ] Registrar Trabajador\n[ 2 ] Registrar Alumno\n[ 3 ] Agregar Materias\n[ 4 ] Regresar"
    opc = validation(msg, 1, 4)

    cursor.execute("SELECT * FROM Alumno")

    return opc


def mostrar():
    msg = "[ 1 ] Mostrar Alumnos\n[ 2 ] Mostrar todos los trabajadores\n[ 3 ] Mostrar Profesores\n[ 4 ] Mostrar Facultades\n[ 5 ] Mostrar Todas las materias\n[ 6 ] Regresar"
    opc = validation(msg, 1, 6)

    return opc

def modificar():
    msg = "[ 1 ] Modificar datos de alumno\n[ 2 ] Modificar datos de trabajador\n[ 3 ] Modificar Materia\n[ 4 ] Regresar"
    opc = validation(msg, 1, 4)

    return opc

def eliminar():
    msg = "[ 1 ] Eliminar un alumno\n[ 2 ] Eliminar trabajador\n[ 3 ] Eliminar Materia\n[ 4 ] Regresar"
    opc = validation(msg, 1, 4)

    return opc
