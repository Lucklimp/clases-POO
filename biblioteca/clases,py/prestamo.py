from datetime import datetime
import detalle_libro
import usuario

class Prestamo(detalle_libro, usuario):
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamo, fecha_devolucion, fecha_efectiva_dev):
        detalle_libro.__init__(isbn)
        usuario.__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_efectiva_dev

    def calcular_fechas(self):
        if(self.n_copias > 0):
            self.fecha_prestamo = datetime.datetime.now()
            dias_de_prestamo = 7
            self.fecha_devolucion = self.fecha_prestamo() + dias_de_prestamo