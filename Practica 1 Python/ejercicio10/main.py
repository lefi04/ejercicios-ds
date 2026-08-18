from biblioteca.modelos.libro import Libro
from biblioteca.servicios.prestamo import (
    realizar_prestamo,
    realizar_devolucion,
    consultar_disponibilidad
)

# Creamos un libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "123456")

# Consultamos disponibilidad
print(consultar_disponibilidad(libro1))

# Realizamos un préstamo
print(realizar_prestamo(libro1))

# Consultamos nuevamente
print(consultar_disponibilidad(libro1))

# Intentamos prestarlo otra vez
print(realizar_prestamo(libro1))

# Realizamos la devolución
print(realizar_devolucion(libro1))

# Consultamos nuevamente
print(consultar_disponibilidad(libro1))