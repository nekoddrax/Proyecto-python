import os
import random
#from Enemy import *
def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

class Jugador:
    def __init__(self):
        self.nivel = 1
        self.vida_jugador = 100
        self.defensa_jugador = 5
        self.daño_jugador = 5
        self.probabilidad_estado = 100
        self.probabilidad_critico = 10
        self.daño_estado = 0
        self.estado = "normal"
        self.inventario = {"pocion": 1}


    def tomar_posion(self):
        if self.inventario["pocion"] > 0:
            self.vida_jugador += 50
            self.inventario["pocion"] -= 1
            print(f"El jugador usa una poción! La vida del jugador ahora es {self.vida_jugador}")
        else:
            print("No tienes pociones en tu inventario")

    def prob_critico(self):
        critico = random.randint(0, 100)
        print("Crítico: ", critico)            
        critico_acertado = False
        self.daño_jugador *= 2
        critico_acertado = True
        print("¡Crítico!")
        print("Fallo")

    def prob_estado(self, enemigo):
        if isinstance(enemigo, Enemigo):
            estado = random.randint(0, 100)
            print("Estado: ", estado)
            if estado <= self.probabilidad_estado:
                enemigo.estado_enemigo = "envenenado"
                print("El estado del enemigo es", enemigo.estado_enemigo)
            else:
                print("Fallo estado")
        else:
            print("El objetivo no es un enemigo")
