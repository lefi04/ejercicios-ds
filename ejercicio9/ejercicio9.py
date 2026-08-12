class CuentaBancaria:

    # Creamos la cuenta
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto a depositar debe ser mayor a 0.")

    # Método para retirar dinero
    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        elif monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes.")

    # Método para mostrar la información
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo:.2f}")


# Creamos dos cuentas
cuenta1 = CuentaBancaria("Vargas")
cuenta2 = CuentaBancaria("Samuel", 5000.0)

# Operaciones sobre la cuenta 1
cuenta1.depositar(10000)
cuenta1.retirar(2500)
cuenta1.mostrar_info()

print()

# Operaciones sobre la cuenta 2
cuenta2.depositar(2000)
cuenta2.retirar(8000)
cuenta2.mostrar_info()
