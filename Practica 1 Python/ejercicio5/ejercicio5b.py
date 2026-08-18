# Definimos la contraseña correcta
CONTRASEÑA_CORRECTA = "Admin1234"

# Contador de intentos
intentos = 0

# Permitimos un máximo de 3 intentos
while intentos < 3:
    contraseña = input("Ingrese la contraseña: ")

    if contraseña == CONTRASEÑA_CORRECTA:
        print("Inicio de sesión exitoso.")
        break

    else:
        intentos += 1
        print("Contraseña incorrecta.")

if intentos == 3:
    print("Demasiados intentos. Usuario bloqueado.")
