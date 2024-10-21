# Ingresar 10 usuarios o participantes
# Cada usuario tiene nombre, Nickname, edad, Ranking, genero, pais
# Se debe ingresar por teclado el nombre del participante LOCAL
# Se debe ingresar por teclado el nombre del participante VISITA
# Luego se selecciona el torneo
# (Mortal kombat 11, FIFA 2025, Street Fighter 6)
# Al ganador se le entrega 5 puntos
# Ingresar MATCH hasta que un usuario llegue a los 30 PTOS

# Mostrar PODIUM del torneo (Ranking, nickname, puntos)

nombre = [0,0,0]
Nickname = [0,0,0]
edad_p = [0,0,0]
Ranking = [0,0,0]
genero_p = [0,0,0]
pais = [0,0,0]
cont_match = 0

def validar_edad():
    while True:
        try:
            edad = input("Ingrese su edad: ")
            print("")
            if (edad > "18" and edad < "50"):
                print("Edad confirmada.")
                print("")
                break
            else:
                print("Edad no dentro de los valores permitidos, intente de nuevo.")
                print("")
        except ValueError:
            print("Edad no confirmada, intente de nuevo.")

def validar_genero():
    while True:
        try:
            genero = input("Ingrese su Sexo: ")
            print("")
            if (genero == "Femenino" or genero == "F" or genero == "Masculino" or genero == "M"):
                print("Genero ingresado correctamente")
                print("")
                break
            else:
                print("Genero no valido, intente de nuevo con ¨Masculino¨ o ¨Femenino¨")
        except ValueError:
            print("Sexo ingresado no valido, intente de nuevo.")


for i in range(0, 10):

    print("Participante", i+1)
    print("")
    nombre[i] = input("Ingrese su nombre: ")
    print("")
    Nickname[i] = input("Ingrese su apodo/Nickname: ")
    print("")
    edad_p[i] = validar_edad()
    print("")
    genero_p[i] = validar_genero()
    pais[i] = input("Ingrese su pais de origen: ")
    puntaje = 0

while puntaje < 30:
    print("Nuevo MATCH")


