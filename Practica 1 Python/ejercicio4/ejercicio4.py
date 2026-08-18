# Función para convertir de Fahrenheit a Celsius
def a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Función para convertir de Celsius a Fahrenheit
def a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Pedimos los datos al usuario
temperatura = float(input("Ingrese la temperatura: "))
escala = input("Ingrese la escala original (C/F): ").upper()

# Realizamos la conversión

if escala == "C":
    resultado = a_fahrenheit(temperatura)
    print(f"La temperatura {temperatura} °C en Fahrenheit es igual a {resultado:.2f} °F")

elif escala == "F":
    resultado = a_celsius(temperatura)
    print(f"La temperatura {temperatura} °F en Celsius es igual a {resultado:.2f} °C")

else:
    print("Escala no válida. Ingrese C o F.")


