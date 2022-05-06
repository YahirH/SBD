import os
import time
import pyodbc
from colorama import Fore
from terminaltables import AsciiTable

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
        1: 'Direccion',
        2: 'Tesoreria',
        3: 'Prefectura',
        4: 'Servicios Generales'
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

    def ejecutar_query(self, query):
        try:
            self.cursor.execute(query)

            self.cnxn.commit()

        except:
            print(Fore.RED + "[ X ] Hubo un error al realizar la consulta a la base de datos.")
            exit()

    def mostrar_query(self, query):
        try:
            return self.cursor.execute(query)
        except:
            print(Fore.RED + "Hubo un error al realizar la consulta a la base de datos.")
            exit()


    def CrearAlumno(self):
        
        nombre = str(input("Nombre del alumno: "))
        edad = int(input("\nEdad del Alumno: "))
        sexo = str(input("\nSexo del alumno: "))

        print("\n============= SELECCIONE LA FACULTAD =================\n")
        count = 1
        for facultades in self.facultades.values():
            print(f"[ {count} ] {facultades['nombre']}")
            count += 1
        idFacultad = int(input("\nSeleccione la facultad: "))

        print("\n============== SELECCIONE LA CARRERA =================\n")
        count = 1
        for carrera in self.facultades[idFacultad]['carrera'].values():
            print(f"[ {count} ] {carrera}")
            count += 1
        carrera = int(input("\nSeleccione la carrera: "))

        idCarrera = list(self.facultades[idFacultad]['carrera'])[carrera-1]
        print(idCarrera)

        query = f"INSERT INTO Alumno(IdFacultad,IdCarrera,Nombre,Edad,Sexo) VALUES ('{idFacultad}','{idCarrera}','{nombre}','{edad}','{sexo}');"
        db.ejecutar_query(self, query)

        os.system("clear")
        print(Fore.GREEN + f"\nEl alumno {nombre} se a registrado con exito!\n")


    def CrearTrabajador(self):
        print("\n============= SELECCIONE LA FACULTAD =================\n")
        count = 1
        for facultades in self.facultades.values():
            print(f"[ {count} ] {facultades['nombre']}")
            count += 1
        idFacultad = int(input("\nSeleccione la facultad: "))

        print("\n============= SELECCIONE EL DEPARTAMENTO =================\n")
        for num,departamento in self.departamentos.items():
            print(f"[ {num} ] {departamento}")

        departamento = int(input("\nSeleccione el departamento: "))

        idDepartamento = list(self.departamentos)[departamento]

        nombre = str(input("\nNombre del Trabajador: "))
        apellidos = str(input("\nApellidos del Trabajador: "))
        edad = int(input("\nEdad del Trabajador: "))
        sexo = str(input("\nSexo del trabajador[H/M]: "))
        area = str(input("\nArea del trabajador: "))

        query = f"INSERT INTO Trabajador(IdDepartamento,IdFacultad,Nombre,Apellidos,Edad,sexo,area) VALUES ('{idDepartamento}','{idFacultad}','{nombre}','{apellidos}','{edad}', '{sexo}', '{area}');"
        db.ejecutar_query(self, query)

        print(Fore.GREEN + f"\nEl alumno {nombre} se a registrado con exito!\n")

    def crearProfesor(self):
        nombre = str(input("Ingrese el nombre del trabajador: "))
        os.system("cls")
        print(f"Buscando a {nombre} en la base de datos, espere...")
        time.sleep(2)
        
        datos = db.mostrar_query(self,f"SELECT * FROM Trabajador WHERE '{nombre}'=Nombre+' '+Apellidos").fetchall()
        
        if len(datos) == 0:
            print("\n" + Fore.RED + "No se obtuvieron resultado(s) en la base de datos.\n")
            return 1
        else:
            print("\n" + Fore.GREEN + "Se obtuvo resultado(s) en la base de datos.\n")

        print(AsciiTable(list(datos)).table)
        
        opc = input("\n¿El trabajador que se muestra es correcto? [S/N]: ")

        if opc == 'S' or opc == 's':
            idTrabajador = datos[0][0]
            print(idTrabajador, type(idTrabajador))
            db.ejecutar_query(self,f"INSERT INTO Docentes(IdTrabajador) VALUES('{idTrabajador}')")
        elif opc == 'N' or opc == 'n':
            return 1


    def mostrarAlumnos(self):
        titulo = [["Id","Nombre","Edad","Sexo","Facultad","Carrera"]]
        registros = db.mostrar_query(self,"SELECT Alumno.Id,Alumno.Nombre,Alumno.Edad,Alumno.Sexo,Facultad.NombreFacultad,Carrera.NombreCarrera FROM Alumno INNER JOIN Facultad ON Alumno.IdFacultad=Facultad.Id INNER JOIN Carrera ON Alumno.IdCarrera=Carrera.Id").fetchall()
        table = AsciiTable(titulo + list(registros))
        print(table.table)

    def mostrarTrabajadores(self):
        titulo = [["Id","Nombre","Apellidos","Edad","Sexo","Departamento","Area"]]
        registros = db.mostrar_query(self,"SELECT Trabajador.Id,Nombre,Apellidos,Edad,Sexo,Departamento.NombreDepartamento,Area FROM Trabajador INNER JOIN Departamento ON Trabajador.IdDepartamento=Departamento.Id").fetchall()
        table = AsciiTable(titulo + list(registros))
        print(table.table)
    
    def mostrarProfesor(self):
        titulo = [["Id","Nombre","Apellidos","Edad","Sexo"]]
        registros = db.mostrar_query(self,"SELECT Docentes.Id,Trabajador.Nombre,Trabajador.Apellidos,Trabajador.Edad,Trabajador.Sexo FROM Docentes INNER JOIN Trabajador ON Docentes.IdTrabajador=Trabajador.Id").fetchall()
        table = AsciiTable(titulo + list(registros))
        print(table.table)


    def mostrarFacultades(self):
        titulo = [["Id","Facultad","Campus",]]
        registros = db.mostrar_query(self,"SELECT Facultad.Id,Facultad.NombreFacultad,Campus.NombreCampus FROM Facultad INNER JOIN Campus ON Facultad.IdCampus=Campus.Id").fetchall()
        table = AsciiTable(titulo + list(registros))
        print(table.table)