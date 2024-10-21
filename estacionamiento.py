# Realizar un programa  que de solucion a lo sgte:
# Ingresar 5 alumnos (nombre, apellido, y 3 notas)
# Calcular el promedio del alumno
# Calcular el promedio total del curso
# (compuesto por estos 5 alumnos)
# Calcular la mejor nota por alumno
# Calcular el mejor promedio

def promedio_curso(n1, n2, n3, n4, n5):
    #Variables locales
    prom = 0
    prom = (n1+n2+n3+n4+n5)/5
    return prom

def promedio_notas(n1,n2,n3,p1,p2,p3):
    # Variables locales
    prom = 0
    prom = (p1*n1+p2*n2+p3*n3)/100
    return prom

# Nota 1 vale 20%
# Nota 2 vale 30%
# Nota 3 vale 50%

# Inicializacion de ARREGLOS
notas = [0,0,0]
alumnos = [0,0,0,0,0]

# Ponderados, que en este caso son CONSTANTES
p = [20,30,50]
prom = [0,0,0,0,0]
print("Welcome to the Insuco School")
print("")

pc = 0

for i in range (0,5):
    print(f"Alumno {i+1}")
    # Ingrese nombre del alumno
    alumnos[i] = (input(f"Ingrese nombre del alumno: "))
    # Notas variables ingresadas por teclado
    notas[0] = float(input("Ingrese primera nota: "))
    notas[1] = float(input("Ingrese segunda nota: "))
    notas[2] = float(input("Ingrese tercera nota: "))
    while ((notas[0,1,2]<1 or notas[0,1,2]>7)):
        if (notas[0,1,2]<1):
            print("Nota muy pequeña, ingrese una nota mas grande")
        if (notas[0,1,2]>7):
            print("Nota muy grande, ingrese una nota mas pequeña")
    except ValueError:

    #Llamada a la funcion
    prom[i] = promedio_notas(notas[0], notas[1], notas[2], p[0], p[1], p[2])
    print(f"El promedio del alumno {alumnos[i]} es ",prom[i])
    print("")
    pc = pc+prom[i]
    Mnota < notas[0]

pc = pc/5

print("El promedio general del curso es de ", pc)
