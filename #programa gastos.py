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
   
def preguntardia():
    cat = ""
    dia = input("Qué día quieres registrar?: ")
    gasto = input("Qué gasto quieres registrar?: ")
    razon = input("A qué se debe el gasto?: ")
    print("¿Qué tipo de gasto es?\n" \
        "---------------------\n" \
        "1) Transporte\n2) Comida\n3) Medicamentos\n4) Música\n5) Caprichos\n6) Videojuegos\n7) Arte\n" \
        "---------------------")
    opc = int(input("Introduce una opción: "))
    if opc <=7:
        if opc == 1:
            print(True)
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
    with open("registrogastos.csv", "a") as fichero:
         fichero.write(f"{dia}\t{gasto}\t{razon}\t{cat}\n")
    
'''
def numerodegastos():
    n = int(input("Cuantos gastos vas a registrar?: "))
    for i in range(0, n):
        preguntardia()
numerodegastos()
'''

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
