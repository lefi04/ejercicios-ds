from ..modelos.libro import Libro


def realizar_prestamo(libro):
    if libro.disponible:
        libro.disponible = False
        return f"El libro '{libro.titulo}' fue prestado."
    else:
        return f"El libro '{libro.titulo}' no está disponible."


def realizar_devolucion(libro):
    if libro.disponible == False:
        libro.disponible = True
        return f"El libro '{libro.titulo}' fue devuelto."
    else:
        return "El libro ya figuraba como disponible."



def consultar_disponibilidad(libro):
    if libro.disponible:
        return f"El libro '{libro.titulo}' está disponible."
    else:
        return f"El libro '{libro.titulo}' no está disponible."