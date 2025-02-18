from actores import Player
from actores import Enemy
import os
import time
import pygame
def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
pygame.init()
# Crear instancias de Jugador y Enemigo
jugador = Player.Jugador()
enemigo = Enemy.Enemigo()
while True:
    print("Vida del jugador: ", jugador.vida_jugador, "\n")
   
    accion = input("Que quieres hacer? \n \n 1. Atacar \n 2. Defender \n 3. Usar poción \n")
    if accion == "1":
        print("\n")
        pygame.mixer.music.load('archivos/Sonido_perdido.mp3')
        pygame.mixer.music.play()
        jugador.atacar()
        time.sleep(2)
        limpar_pantalla()
    elif accion == "2":
        print("\n")
        jugador.defender()
        time.sleep(2)
        limpar_pantalla()
    elif accion == "3":
        print("\n")
        jugador.usar_pocion()
        time.sleep(2)
        limpar_pantalla()
    elif accion == "4":
        jugador.vida_jugador = 0
    
    
    else:
        print("Comando no válido")
        time.sleep(2)
        limpar_pantalla()
   
    if jugador.vida_jugador <= 0:
        limpar_pantalla()
        print("Has perdido")
        break