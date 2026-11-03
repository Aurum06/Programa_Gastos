#programa gastos
#Sistema de guardados
import sqlite3

class GestorGastosDB: #clase encargada de gestionar datos y operaciones de escritura y lectura
    def __init__(self, db_name="gastos.db"): #crea el archivo
        self.db_name = db_name 
        self._crear_tabla()

    def _conectar(self):
        return sqlite3.connect(self.db_name)

    def _crear_tabla(self): #inicializa las columnas de la tabla
        with self._conectar() as conn: #abre la conexión y se asegura de que se cierre si hay errores
         cursor = conn.cursor() #crea un cursor, objeto necesario para interactuar con la base de datos
         cursor.execute("""
                CREATE TABLE IF NOT EXISTS gastos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    gasto REAL NOT NULL,
                    razon TEXT,
                    categoria TEXT
                )
            """)
         conn.commit()
    def guardarGasto(self, fecha:str, gasto:float, razon:str, cat:str):
        try:
            with self._conectar() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO gastos (fecha, gasto, razon, categoria)
                    VALUES (?, ?, ?, ?)
                """, (fecha, gasto, razon, cat))
                conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error de guardado: {e}")
            return False
    

def borrarloescrito():
     borrar = input("Deseas borrar lo escrito?(Y/N): ")
     borrar = borrar.upper()
     if borrar in "Yes":
          conf = input("Seguro?, Este proceso no es reversible: ")
          conf = conf.upper()
          if conf in "Yes":
           with open("registrogastos.csv", "w") as fichero:
               print("Contenido borrado")
          else:
              print("Se ha mantenido el contenido anterior")
     else:
         print("Se ha mantenido el contenido anterior")
   
def preguntardia():
    db = GestorGastosDB()
    l = []
    cat = ""
    dia = input("Qué día quieres registrar?: ")
    rep = True
    while rep == True :
     gasto = input("Qué gasto quieres registrar?: ")
     razon = input("A qué se debe el gasto?: ")
     print("¿Qué tipo de gasto es?\n" \
        "---------------------\n" \
        "1) Transporte\n2) Comida\n3) Medicamentos\n4) Música\n5) Caprichos\n6) Videojuegos\n7) Arte\n" \
        "---------------------")
     opc = int(input("Introduce una opción: "))
     if  opc <=7 and opc > 0:
        if opc == 1:
            cat = "Transporte"
        elif opc == 2:
            cat = "Comida"
        elif opc == 3:
            cat = "Medicamentos"
        elif opc == 4:
            cat = "Música"
        elif opc == 5:
            cat = "Caprichos"
        elif opc == 6:
            cat ="Videojuegos"
        elif opc == 7:
            cat = "Arte"
        if db.guardarGasto(dia, gasto, razon, cat):
            print("Gasto guardado con éxito")
     else:
      print("Opción no válida")
     masgastos = input("¿Quieres añadir algún pago más para ese mismo día?: (Y/N): ")
     masgastos = masgastos.upper()
     if masgastos in "Yes": 
         rep = True
     elif masgastos in "No":
         rep = False
         print("---------------------------------------\n          PROGRAMA FINALIZADO\n" \
         "---------------------------------------")
         break
    
    

def menu():
    print("Bienvenido al registro de tus gastos. ¿Qué deseas hacer?\n------------------------------------" \
    "---------------------\n" \
    "1)Añadir un gasto\n2)Añadir una devolución\n3)Recuento de gastos de este mes\n4)Recuento de gastos de todo el año\n5)Borrar todo\n"
    "---------------------------------------------------------")
    cont = 0
    while cont == 0:
     opcion = input("Introduce una opción: ")
     if opcion in "12345": 
        if opcion == "1":
            preguntardia()
            cont = 1
        elif opcion == "2":
            print("No implementado, prueba otra vez")
            cont = 0
        elif opcion == "3":
            print("No implementado, prueba otra vez")
            cont = 0
        elif opcion == "4":
            print("No implementado, prueba otra vez")
            cont = 0
        elif opcion == "5":
            borrarloescrito()
            cont = 1
menu()

if __name__ == "__main__":
    preguntardia()


    