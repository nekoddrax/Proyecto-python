#estadistica de moustruo estandar 
from jugador import vida_jugador, defensa_jugador
vida_enemigo = 100
daño_enemigo = 10
probabilidad_estado_enemigo = 0
probabilidad_critico_enemigo = 0
estado_enemigo = ("normal")

def ataque():
    ataque =- (vida_jugador + defensa_jugador) - daño_enemigo
    
