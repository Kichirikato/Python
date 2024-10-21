# Ingresar N personajes para un Show en la pampilla (N ingresado por teclado)
# Ingresar por personaje lo sgte:
# Nombre
# Apellido
# Sueldo(Rango de 1.000.000 y 17.000.000 (validar))
# Fecha de su espectaculo (las opciones son: 17 septiembre, 18 septiembre, 19 septiembre, 20 septiembre (validar))
# Calcular promedio y nombre completo
# Calcular cual es el artista que mas se le pago

nombre = [0,0,0]
apellido = [0,0,0]
artista_p =[0,0,0]
sueldo_p = [0,0,0]
horario_p = [0,0,0]
pa1 = 0
pa2 = 0
pa3 = 0
pa4 = 0
pa5 = 0

def validar_artista():
    while True:
        try:
            print("A cual artista quiere ver?")
            print("1: Adam Sandler")
            print("2: Bruno Dias")
            print("3: The Rock")
            print("4: Spider-Man")
            print("5: Jim Carrey")
            artista = input("Eliga su artista: ")
            if (artista == "1" or artista == "2" or artista == "3" or artista == "4" or artista == "5"):
                print("Eleccion ingresada correctamente")
                print("")
                break
            else:
                print("No se pudo validar la eleccion, intente de nuevo")
        except ValueError:
            print("No se pudo validar su eleccion, intente de nuevo")


def validar_sueldo():
    while True:
        try:
            sueldo = float(input("Ingrese sueldo de la persona: "))
            print("")

            if sueldo >= 1000000 and sueldo <= 17000000:
                print("Sueldo ingresado correctamente.")
                break
            else:
                print("Sueldo no valido,intente de nuevo")
        except ValueError:
            print("Ese sueldo no es valido. Intenta de nuevo.")
            

def validar_horario():
    while True:
        try:
            print("Eliga dia de la funcion: ")
            print("1: 17 de septiembre")
            print("2: 18 de septiembre")
            print("3: 19 de septiembre")
            print("4: 20 de septiembre")
            horario = input("Opcion a elegir: ")
            print("")
            
            if horario == "1" or horario == "2" or horario == "3" or horario == "4":
                print("Opcion validada.")
                print("")
                print("Elija su hora de funcion:")
                print("1: 11:00")
                print("2: 13:00")
                print("3: 18:00")
                print("4: 21:00")
                fecha = input("Seleccione una alternativa: ")

                if fecha == "1" or fecha == "2" or fecha == "3" or fecha == "4":
                    print("Elecciones completadas y verificadas.")
                    break
                else:
                    print("Numero no valido, selecciona un horario correcto.")
            else:
                print("Opcion no valida, intente de nuevo")
        except ValueError:
            print("Opcion no validada")



N = int(input("Ingrese cantidad de personas a ingresar en el show: "))
print("")

for i in range(0,N):
    nombre[i] = input("Ingrese nombre de la persona: ")
    print("")

    apellido[i] = input("Ingrese apellido de la persona: ")
    print("")

    artista_p[i] = validar_artista()
    sueldo_p[i] = validar_sueldo()
    horario_p[i] = validar_horario()


