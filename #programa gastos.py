#programa gastos
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
borrarloescrito()

def preguntardia():
    dia = input("Qué día quieres registrar?: ")
    gasto = input("Qué gasto quieres registrar?: ")
    razon = input("A qué se debe el gasto?: ")
    with open("registrogastos.csv", "a") as fichero:
         fichero.write(f"{dia}\t{gasto}\t{razon}\n")
preguntardia()
    
'''
def numerodegastos():
    n = int(input("Cuantos gastos vas a registrar?: "))
    for i in range(0, n):
        preguntardia()
numerodegastos()
'''

