import os
import time
import random
def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jugador:
    def __init__(self):
        self.nivel = 1
        self.vida_jugador = 100
        self.defensa_jugador = 20
        self.daño_jugador = 20
        self.probabilidad_estado = 0
        self.probabilidad_critico = 50
        self.daño_estado = 0
        self.estado = "normal"
        self.inventario = {"pocion": 1}

perro = 10
def critico():
    Critico = random.randint(0, 100)
    print(Critico)
    if Critico <= perro:
        
        print("Critico!") 
    else:
        print("fallo")
