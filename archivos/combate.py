from actores import Player
from actores import Enemy
import os
import time

def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

turno = 1
# Crear instancias de Jugador y Enemigo
jugador = Player.Jugador()
enemigo = Enemy.Enemigo()
while True: 
    print("Vida del jugador: ", jugador.vida_jugador, "\n")
    def turno_jugador(): 
        accion = input("Que quieres hacer? \n \n 1. Atacar \n 2. Defender \n 3. Usar poción \n")
        if accion == "1":
            print("\n")  
            time.sleep(2)
        elif accion == "2":
            print("\n")
            jugador.defender()
            time.sleep(2)
        elif accion == "3":
            print("\n")
            jugador.usar_pocion()
            time.sleep(2)
        else:
            print("Comando no válido")
            time.sleep(1)

    def turno_enemigo():
        jugador.vida_jugador -= enemigo.daño_enemigo
        time.sleep(2)
        limpar_pantalla()


    if turno == 1:
        turno_jugador()
        limpar_pantalla()
        turno = 2
    elif turno == 2:
        turno_enemigo()
        turno = 1

    if jugador.vida_jugador <= 0:
        limpar_pantalla()
        print("Has perdido")
        time.sleep(2)
        break
