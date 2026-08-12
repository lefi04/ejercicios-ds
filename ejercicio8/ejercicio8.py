def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):

    if precio_base <= 0:
        raise ValueError("El precio base debe ser positivo.")

    if porcentaje_descuento < 0:
        raise ValueError("El porcentaje de descuento no puede ser negativo.")

    # Aplicamos el descuento
    precio_final = precio_base - (precio_base * porcentaje_descuento / 100)

    # Si es VIP, aplicamos un 5% extra sobre el precio ya rebajado
    if es_vip:
        precio_final = precio_final - (precio_final * 5 / 100)
    return precio_final


# Pruebas

print(calcular_precio_final(1000))
print(calcular_precio_final(1000, 20))
print(calcular_precio_final(1000, 20, True))
