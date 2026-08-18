# Pedimos la contraseña
contraseña = input("Ingrese una contraseña: ")

# Comprobamos que tenga al menos 8 caracteres
tiene_longitud = len(contraseña) >= 8

# Comprobamos si tiene mayúsculas y minúsculas
tiene_mayuscula = False
tiene_minuscula = False

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True

    if caracter.islower():
        tiene_minuscula = True

# Verificamos las tres condiciones
if tiene_longitud and tiene_mayuscula and tiene_minuscula:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")

    if not tiene_longitud:
        print("- Debe tener al menos 8 caracteres.")

    if not tiene_mayuscula:
        print("- Debe contener al menos una letra mayúscula.")

    if not tiene_minuscula:
        print("- Debe contener al menos una letra minúscula.")
