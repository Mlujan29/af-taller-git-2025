#       FUNCIONES
def alta(cod,descripcion,precio,productos):
    if cod in productos:                        #si el codigo ya existe (ya que debe de ser único)
        print("ALERTA: El codigo ya existía ¿Desea sobrescribirlo? El Stock volverá a cero")
        confirmación = input("[S/N]: ")         #guarda la respuesta
        if confirmación.upper() == 'S' or confirmación.upper() == "SI":
            productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
            print(f"OK: ALTA {cod} - {descripcion}")
        elif confirmación.upper() == 'N' or confirmación.upper() == "NO":       #si dice que no vuelve al comienzo
            return
        else:                   #si ingresa cualquier otra cosa
            print("ERROR: La confirmación no fue válida")
    else:
        productos[cod] = {"descripcion": descripcion, "precio": precio, "stock": 0}
        print(f"OK: ALTA {cod} - {descripcion}")


def stock(cod, cantidad, productos):
    if cod in productos:                            #verifica que el codigo ingresado exista
        productos[cod]["stock"] += cantidad
        if cantidad > 0:
            print(f"OK: STOCK {cod} --> +{cantidad}")
        else:
            print(f"OK: STOCK {cod} --> {cantidad}")
    else:
        print("ERROR: El código ingresado no existe")


def promos_activas():               # muestra las promociones
    print("""PROMOCIONES ACTIVAS:
    1) 3x2 en chicle
    2) 10% en agua500 desde 5 unidades
    3) Descuento de 1000 Gs en venta conjunta de galleta y cafe""")


#   MAIN
productos =  {}     # Donde se van a almacenar los productos

PROMOCIONES = [                     # Definición de las promociones
    {
        'tipo': '3x2', 
        'producto': 'chicle'
    },
    {
        'tipo': '10%', 
        'producto': 'agua500', 
        'min_cantidad': 5
    },
    {
        'tipo': 'combo_fijo', 
        'productos': ['galleta', 'cafe'], 
        'descuento': 1000
    }
]

movimientos = []                # Registra los movimientos

while True:
    print("Acciones: ALTA, STOCK, VENDE, DEVUELVE, PROMOS, REPORTE, FIN")
    entrada = input("Realizar: ")

    if entrada.strip():     #verifica que la entrada no este vacia

        partes = entrada.split()
        match partes[0].upper():
            case "ALTA":
                if len(partes) == 4:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    descripcion = partes[2]

                    try:
                        precio =  int(partes[3])
                        if precio <= 0:                     #para rechazar la accion si el precio es negaivo o cero
                            print("ERROR: Ingrese un precio válido")
                        else:
                            alta(cod,descripcion,precio,productos)
                    except ValueError:
                        print("ERROR: El precio debe de ser un número")
                
                else:
                    print("ERROR: Ingrese el formato correcto para dar alta al producto")
            
            case "STOCK":
                if len(partes) == 3:    #validación en caso de que no se ingrese en el formato correcto
                    cod = partes[1]
                    
                    try:
                        cantidad = int(partes[2])       #la cantidad si puede ser negativa, en caso de que algo le pase al stock ya definido
                        stock(cod,cantidad,productos)
                    except ValueError:
                        print("ERROR: La cantidad debe de ser un número")
                
                else:
                    print("ERROR: Ingrese el formato correcto para dar stock al producto")

            case "VENDE":
                print("la funcion")

            case "DEVUELVE":
                print("la funcion")

            case "PROMOS":
                promos_activas()

            case "REPORTE":
                print("la funcion")

            case "FIN":                            # cierra el programa
                print("Gracias por usar el programa! Adiós...")
                break

            case _:     # si se ingresa cualquier otra palabra
                print("Introduzca una acción válida")
    
    else:
        print("ERROR: No se ingresó nada")