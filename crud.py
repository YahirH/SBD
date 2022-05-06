from tkinter import N
from colorama import Fore
import pyodbc
class db():

    # Id Facultades
    facultades = {
        1: {'nombre': 'FCFM', 'id': 1, 'carrera': {1: 'LSTI', 2: 'LCC', 3: 'LA'}},
        2: {'nombre': 'FCQ', 'id': 2, 'carrera': {4: 'LQFB', 5: 'IIA'}},
        3: {'nombre': 'FIME', 'id': 3, 'carrera': {6: 'ITS', 7: 'IAS', 8: 'IA'}},
        4: {'nombre': 'FCC', 'id': 4, 'carrera': {9: 'LCC', 10: 'LMGI'}},
        5: {'nombre': 'FAV', 'id': 5, 'carrera': {11: 'LDG'}},
        6: {'nombre': 'FACMED', 'id': 6, 'carrera': {12: 'MED'}},
    }

    departamentos = {
        'Direccion': 1,
        'Tesoreria': 2,
        'Prefectura': 3,
        'Servicios Generales': 4
    }


    def __init__(self, driver="{ODBC Driver 17 for SQL SERVER}", server="LENOVO\SQLEXPRESS", database="UANAL", username="Python", pwd="1234"):
        self.driver = driver
        self.server = server
        self.database = database
        self.username = username
        self.pwd = pwd

        try:
            self.cnxn = pyodbc.connect('DRIVER='+self.driver
                                      +';SERVER='+self.server
                                      +';DATABASE='+self.database
                                      +';UID='+self.username
                                      +';PWD='+self.pwd+'')
        except:
            print(Fore.RED + "[ X ] Oops! hubo un error al conectar con la base de datos...")

        self.cursor = self.cnxn.cursor()


    def close_connection(self):
        try:
            self.cnxn.close()
        except:
            print(Fore.RED + "[ X ] Oops! hubo un error al cerrar la base de datos...")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)

            self.cnxn.commit()
        except:
            print(Fore.RED + "Hubo un error al realizar la consulta a la base de datos.")


    def CrearAlumno(self):
        
        nombre = str(input("Nombre del alumno: "))
        edad = int(input("\nEdad del Alumno: "))
        sexo = str(input("\nSexo del alumno: "))

        print("\n============= SELECCIONE LA FACULTAD =================")
        count = 1
        for facultades in self.facultades.values():
            print(f"[ {count} ] {facultades['nombre']}")
            count += 1
        idFacultad = int(input("\nSeleccione la facultad: "))

        print("\n============== SELECCIONE LA CARRERA =================")
        count = 1
        for carrera in self.facultades[idFacultad]['carrera'].values():
            print(f"[ {count} ] {carrera}")
            count += 1
        idCarrera = int(input("\nSeleccione la carrera: "))

        query = f"INSERT INTO Alumno(IdFacultad,IdCarrera,Nombre,Edad,Sexo) VALUES ('{idFacultad}','{idCarrera}','{nombre}','{edad}','{sexo}');"
        db.execute_query(self, query)

        print(Fore.GREEN + f"\nEl alumno {nombre} se a registrado con exito!\n")


    def CrearTrabajador(self):
        Id = int(input("Id del Trabajador: "))
        idDepartamento = int(input("Id del departamento: "))
        nombre = str(input("Nombre del Trabajador: "))
        apellidos = int(input("Apellidos del Trabajador: "))
        edad = int(input("Edad del Trabajador: "))
        sexo = str(input("Sexo del trabajador: "))
        area = str(input("Area del trabajador: "))

        query = f"INSERT INTO Trabajador(Id,IdDepartamento,Nombre,Apellidos,Edad,sexo,area) VALUES ('{Id}','{idDepartamento}','{nombre}','{apellidos}','{edad}', '{sexo}', '{area}');"
        db.execute_query(self, query)


    def CrearMaterias(self):
        Id = int(input("Id de la materia: "))
        idSemestre = int(input("Id del semestre: "))
        nombre = str(input("Nombre de la materia: "))

        query = f"INSERT INTO Asignatura(Id,IdSemestre,Nombre) VALUES ('{Id}','{idSemestre}','{nombre}')"
        db.execute_query(self, query)