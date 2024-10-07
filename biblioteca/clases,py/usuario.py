import tipo_usuario
from rut_chile import rut_chile
class Usuario(tipo_usuario):
    def __init__(self, id_usuario, nombre_usuario, apellido, fecha_nacimiento, telefono_usuario, rut_usuario, id_tipo_usuario):
        tipo_usuario.__init__(id_tipo_usuario)
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono_usuario = telefono_usuario
        self.rut_usuario = rut_usuario
    
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)