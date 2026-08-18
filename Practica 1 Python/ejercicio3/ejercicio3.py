# Pedimos los datos al usuario

pasaje = float(input("Costo del pasaje: "))
alojamiento = float(input("Costo de alojamiento por noche: "))
noches = int(input("Cantidad de noches: "))
dinero = float(input("Dinero disponible: "))

# Calculamos el costo total
costo_total = pasaje + (alojamiento * noches)

# Comprobamos si alcanza el dinero
es_suficiente = dinero >= costo_total

# Calculamos el saldo
saldo = dinero - costo_total

# Mostramos el resumen

print("\n--- Resumen del viaje ---")
print(f"Costo del pasaje: ${pasaje}")
print(f"Alojamiento: ${alojamiento} x {noches} noches")
print(f"Costo total: ${costo_total}")
print(f"Dinero disponible: ${dinero}")

if es_suficiente:
    print("¿El dinero es suficiente?: Sí")
    print(f"Saldo restante: ${saldo}")
else:
    print("¿El dinero es suficiente?: No")
    print(f"Dinero faltante: ${abs(saldo)}")

