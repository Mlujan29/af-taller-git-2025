## Este archivo se usa para hacer un calculo de cada promocion

def calcular_descuento(items_de_venta,productos,promociones):
    descuento_total =  0                #acuulador para calcular el descuento total

    for promo in promociones:       #analizamos las promociones

        if promo['tipo'] == "3x2" and promo['producto'] ==  "chicle":
            for (codigo, cantidad) in items_de_venta:                           #analizamos lo que se vendió
                if codigo == "chicle":
                    cantidad_gratis = cantidad // 3         #para que el resultado sea entero
                    descuento_total +=  cantidad_gratis * productos['chicle']['precio']
        
        elif promo['tipo'] == "10%" and promo['producto'] ==  "agua500":
            for (codigo, cantidad) in items_de_venta:       #recorre los productos
                if codigo == "agua500":
                    if cantidad >= promo['min_cantidad']:   #solo aplica si es mayor o igual a 5 la compra
                        sin_descuento = cantidad * productos['agua500']['precio']       #primero calculamos el precio original
                        descuento_total += sin_descuento * 0.10         #luego aplicamos el descuento

        elif promo['tipo'] == "combo_fijo":
            codigos = []        #para apartar los codigos de cada producto vendido
            for (codigo,cantidad) in items_de_venta:
                codigos.append(codigo)      #añadimos los codigos
            items_promocion = promo['productos']    #traemos los productos del combo para comparar con los que estan en la lista
            if items_promocion[0] in codigos and items_promocion[1] in codigos:
                descuento_total += promo['descuento']
    
    return int(descuento_total)     #devolvemos el resultado final de descuento