# Estadísticas de monstruo estándar

class Enemigo:
    def __init__(self):
        self.vida_enemigo = 1000
        self.daño_enemigo = 5
        self.probabilidad_estado_enemigo = 0
        self.probabilidad_critico_enemigo = 0
        self.estado_enemigo = "normal"
        self.enemigo_type = "demonio"
print("Enemigo creado")