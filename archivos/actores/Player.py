import os
import time

def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jugador:
    def __init__(self):
        self.nivel = 1
        self.vida_jugador = 100
        self.defensa_jugador = 10
        self.daño_jugador = 10
        self.probabilidad_estado = 0
        self.probabilidad_critico = 0
        self.daño_estado = 0
        self.estado = "normal"
        self.inventario = {"pocion": 1}

    def atacar(self):
        print("El jugador ataca!")

    def defender(self):
        print("El jugador se defiende!")
        
    def usar_pocion(self):
        if self.inventario["pocion"] > 0:
            self.vida_jugador += 20
            self.inventario["pocion"] -= 1
            print(f"El jugador usa una poción! La vida del jugador ahora es {self.vida_jugador}")
        else:
            print("No tienes pociones en tu inventario")
print("hola")