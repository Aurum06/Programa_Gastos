#programa gastos
def preguntardia():
    dia = input("Qué día quieres registrar?: ")
    gasto = input("Qué gasto quieres registrar?: ")
    razon = input("A qué se debe el gasto?")
    with open("registrogastos.ods", "w") as fichero:
         fichero.write(f"{dia}\n{gasto}\t{razon}")    
preguntardia()

with open ("registrogastos.ods", "r") as fichero:
    print(fichero.read())