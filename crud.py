from colorama import Fore
import pyodbc
                     

class db():
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
            print("Error al insertar los datos")

    def CrearAlumno(self, Id, idFacultad, idCarrera, nombre, edad, sexo):
        query = f"INSERT INTO Alumno(Id,IdFacultad,IdCarrera,Nombre,Edad,Sexo) VALUES ('{Id}','{idFacultad}','{idCarrera}','{nombre}','{edad}','{sexo}');"
        db.execute_query(self, query)

    def CrearTrabajador(self, Id, idDepartamento, nombre, apellidos, edad, curp, sexo, area):
        query = f"INSERT INTO Trabajador(Id,IdDepartamento,Nombre,Apellidos,Edad,CURP,sexo,area) VALUES ('{Id}','{idDepartamento}','{nombre}','{apellidos}','{edad}','{curp}', '{sexo}', '{area}');"
        db.execute_query(self, query)