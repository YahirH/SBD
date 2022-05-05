import crud

# Inicializar Crud
app = crud.db()
app.CrearAlumno(2,1,1,"Prueba2",21,"H")
app.close_connection()