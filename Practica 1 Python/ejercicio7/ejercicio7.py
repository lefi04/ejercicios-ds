def analizar_temperaturas(registros):

    # Calculamos el máximo y el mínimo
    maximo = max(registros)
    minimo = min(registros)

    # Calculamos el promedio
    promedio = sum(registros) / len(registros)

    # Retornamos los tres valores en una tupla
    return maximo, minimo, promedio


# Datos de prueba
temperaturas = [25, 30, 18, 22, 27]

# Desempaquetamos
maximo, minimo, promedio = analizar_temperaturas(temperaturas)

# Imprimimos
print(f"Temperatura máxima: {maximo}°C")
print(f"Temperatura mínima: {minimo}°C")
print(f"Temperatura promedio: {promedio:.2f}°C")
