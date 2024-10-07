import libro
import editorial

class DetalleLibro(libro, editorial):
    def __init__(self, id_detalle_libro, isbn, id_editorial, numero_paginas, n_copias, edicion):
        libro.__init__(isbn)
        editorial.__init__(id_editorial)
        self.id_detalle_libro = id_detalle_libro
        self.numero_paginas = numero_paginas
        self.n_copias = n_copias
        self.edicion = edicion