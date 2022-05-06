# External modules
from colorama import init, Fore
import time
import os
# Local modules
import crud

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

def salir_regresar(funcion):
    opc = int(input("\n[1] Regresar\t[2] Salir\n\nSeleccione una opcion: "))
    if opc == 1:
        funcion()
    else:
        exit()

def crear():
    msg = "[ 1 ] Registrar Alumno\n[ 2 ] Registrar Trabajador\n[ 3 ] Dar de alta un profesor\n[ 4 ] Regresar"
    opc = validation(msg, 1, 4)

    clear()
    if opc == 1:
        app.CrearAlumno()
        time.sleep(1)
    elif opc == 2:
        app.CrearTrabajador()
    elif opc == 3:
        app.crearProfesor()
    else:
        menu()

    salir_regresar(crear)

def mostrar():
    msg = "[ 1 ] Mostrar Alumnos\n[ 2 ] Mostrar todos los trabajadores\n[ 3 ] Mostrar Profesores\n[ 4 ] Mostrar Facultades\n[ 5 ] Regresar"
    opc = validation(msg, 1, 6)

    clear()
    if opc == 1:
        print("Mostrando tabla de Alumnos...\n\n")
        time.sleep(2)
        app.mostrarAlumnos()
    elif opc == 2:
        print("Mostrando tabla de Trabajadores...\n\n")
        time.sleep(2)
        app.mostrarTrabajadores()
    elif opc == 3:
        print("Mostrando tabla de Profesores...\n\n")
        time.sleep(2)
        app.mostrarProfesor()
    elif opc == 4:
        print("Mostrando tabla de Facultades...\n\n")
        time.sleep(2)
        app.mostrarFacultades()
    else:
        menu()

    salir_regresar(mostrar)

def modificar():
    msg = "[ 1 ] Modificar datos de alumno\n[ 2 ] Modificar datos de trabajador\n[ 3 ] Regresar"
    opc = validation(msg, 1, 4)

    if opc == 1:
        pass
    elif opc == 2:
        pass
    else:
        modificar()

    salir_regresar(modificar)

def eliminar():
    msg = "[ 1 ] Eliminar un alumno\n[ 2 ] Eliminar trabajador\n[ 4 ] Regresar"
    opc = validation(msg, 1, 4)

    if opc == 1:
        pass
    elif opc == 2:
        pass
    else:
        eliminar()

    salir_regresar(eliminar)


if __name__ == '__main__':

    # Inicializar Crud
    app = crud.db()
    
    menu()

    app.close_connection()