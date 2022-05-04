import os
import time
import pyodbc

def clear():
    os.system("cls")

clear()

Servidor = ""
Db = "UANAL"
Usuario = ""
Clave = ""

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+Servidor+';DATABASE='+Db+';UID='+Usuario+';PWD='+Clave)
    print("Conexion a base de datos correctamente...")
    time.sleep(5)
    clear()
except:
    print("No se ah podido conectar a la base de datos.")
    exit()