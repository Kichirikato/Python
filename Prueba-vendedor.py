# Nombre del vendedor
# Apellido del vendedor
# Nombre del cliente
# Apellido del cliente
# Cantidad que va a comprar el cliente (en kgs)
# Fruta que va a comprar el usuario
# Precio de la fruta(en pesos chilenos, por kilo)
# Con cuanto pago el cliente

fruta = [0,0,0]
nombre_vendedor = [0,0,0]
apellido_vendedor = [0,0,0]
nombre_cliente = [0,0,0]
apellido_cliente = [0,0,0]


def validar_fruta():
    frutas_validas = ["1", "2", "3", "4", "5", "0"]

    while True:
        
        print("Frutas disponibles:")
        print("1. Manzana-> $700")
        print("2. Naranja-> $900")
        print("3. Melon-> $1000")
        print("4. Sandia-> $1500")
        print("5. Pera-> $600")
        print("0. Terminar Compras")
        fruta = input("Por favor, ingresa tu fruta: ").lower()
        print("") 
        if fruta in frutas_validas:
            print(f"Fruta '{fruta}' es válida.")
            break
        else:
            print("Fruta no válida. Inténtalo de nuevo.")





c = int(input("Ingrese cuantos clientes son en total: "))
print("")

precio_t = 0

for o in range(1, c+1):

    print("Datos Cliente", o)
    nombre_vendedor[o]= input("Ingrese nombre del Vendedor: ")
    print("")
    apellido_vendedor[o] = input("Ingrese Apellido del Vendedor: ")
    print("")
    nombre_cliente[o] = input("Ingrese nombre del Cliente: ")
    print("")
    apellido_cliente[o] = input("Ingrese Apellido del Cliente: ")
    print("")


    while True:
        validar_fruta()
        kilo = input("cuantos kiloooooooos llevaras: ")
        fruta = {"1": 700, "2": 900, "3": 1000, "4": 1500, "5": 600} 
        precio_total = precio_total+precio_unitario
        respuesta = input("¿Quieres salir? (s/n): ")
        if respuesta.lower() == 's':
            break
        if respuesta.lower() == 'n':
            validar_fruta()
            kilo = input("cuantos kiloooooooos llevaras: ")
            precio_unitario = fruta*kilo
            

    print("El monto a pagar es de ", precio_t, "dolares")
    print("")
    P_cliente = input("Con cuanto paga el cliente: ")
