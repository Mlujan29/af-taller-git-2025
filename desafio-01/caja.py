#Implementa un CLI que lea comandos desde stdin (uno por línea) hasta recibir FIN. El sistema debe mantener 
# un inventario en memoria y un registro de ventas.

def alta(lista,productos):
    if len(lista) == 4:
        productos[lista[1]] = {"descripcion": lista[2], "precio": lista[3], "stock": 0}
        print(f"OK: {productos}")
    else:
        return print("Faltan datos para dar alta al producto")

productos = {}

print("-------------------Caja de Kiosco-------------------")
while True:
    print("Acciones: ALTA, STOCK, VENDE, DEVUELVE, REPORTE, FIN")
    entrada = input("Realizar: ")
    if entrada.strip():
        partes = entrada.split()
        match partes[0].upper():
            case "ALTA":
                alta(partes, productos)
            case "STOCK":
                print("aca va la funcion")
            case "VENDE":
                print("aca va la funcion")
            case "DEVUELVE":
                print("aca va la funcion")
            case "REPORTE":
                print("aca va la funcion")
            case "FIN":
                print("Gracias por usar el programa! Adiós...")
                break
            case _:
                print("ERROR: Ingrese una entrada válida")
    else:
        print("ERROR: No se ingresó nada")