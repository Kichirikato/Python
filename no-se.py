# Inicializando los arreglos ARRAYS o listas
nombre =[0,0,0]
especialidad=[0,0,0]
nota=[0,0,0]
edad=[0,0,0]
mesada=[0,0,0]

def validar_especialidad():
 especialidades_validas = ('programacion', 'administracion', 'contabilidad')

 while True:
     especialidad[i] = input("Introduce tu especialidad (programacion, administracion o contabilidad): ")

     if especialidad in especialidades_validas:
        print("Asignacion '{especialidad}' Validada correctamente")
        return especialidad
     else:
       print("Opcion no valida, Por favor, intente de nuevo.")


# Se recorren con ciclo FOR
for i in range(0,3,1): # 0, 1, 2
    print("Datos ALUMNO", i+1)
    nombre[i]= input("Ingrese nombre del alumno: ")
    edad[i] = input("Ingrese edad del alumno: ")
    nota[i] = input("Ingrese nota del alumno: ")
    mesada[i] = int(input("Ingrese mesada del alumno: "))

def Validar_nota():
   nota = 0 # Inicialmente fuera del rango deseado
   while ((nota < 1) or (nota > 7)):
      nota = float(input("Ingrese nota del alumno: "))
      if nota < 1:
         print("Nota muy pequeña, debe ser mayor o igual que 1.0")
      if nota > 7:
         print("Nota muy grande, debe ser menor o igual que 7.0")
   return nota

def Validar_edad():
   edad = 0 # Inicialmente fuera del rango deseado
   while ((edad < 10) or (edad > 20)):
      try:
         edad = int(input("Ingrese edad del alumno: "))
         if edad < 10:

            print("La edad no es positiva... Intentelo de nuevo")
         if edad > 20:

            print("La edad muy grande, debe ser menor o igual que 20")
      except ValueError:
         return edad

def promedio (a,b,c):
   prom = (a + b + c)/3
   return prom



# FOR para imprimir ARRAY
for i in range(0,3,1):
 print("ALUMNO ",i+1,": ",nombre(i))
 print("ESPECIALIDAD ",i+1,": ",especialidad(i))
 print("EDAD ",i+1,": ", edad(i))
 print("NOTA ",i+1,": ",nota(i))
 print("MESADA ",i+1,": ",mesada(i))
 print("")
print("")
