# Estadísticas de monstruo estándar

class Enemigo:
    def __init__(self):
        self.vida_enemigo = 100
        self.daño_enemigo = 25
        self.probabilidad_estado_enemigo = 0
        self.probabilidad_critico_enemigo = 0
        self.estado_enemigo = "normal"
        self.enemigo_type = "demonio"
print("Enemigo creado")