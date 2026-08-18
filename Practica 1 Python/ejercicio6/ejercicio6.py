while True:

    # Mostramos el menú
    print("\n--- MENÚ ---")
    print("1. Sumar los primeros N números naturales")
    print("2. Encontrar números divisibles por 3")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            n = int(input("Ingrese un número N: "))
            suma = 0
            for numero in range(1, n + 1):
                suma += numero
            print(f"La suma de los primeros {n} números es: {suma}")

        case "2":
            inicio = int(input("Ingrese el inicio del rango: "))
            fin = int(input("Ingrese el final del rango: "))

            print("Números divisibles por 3:")

            for numero in range(inicio, fin + 1):
                if numero % 3 == 0:
                    print(numero)

        case "3":
            print("Programa finalizado.")
            break

        # Si se ingresa otra opción
        case _:
            print("Opción no válida.")
