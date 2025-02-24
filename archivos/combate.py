#from archivos.actores import Player
#from archivos.actores import Enemy
from actores import Player
from actores import Enemy
import os
import time
import random

def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

turno = 1
# Crear instancias de Jugador y Enemigo
jugador = Player.Jugador()
enemigo = Enemy.Enemigo()

while True:
    try:
        print("Vida del jugador: ", jugador.vida_jugador, "\n")
        print("""
          0           /\\___/\\
         /|\\         / 0   0 \\
         / \\        /_________\\
        """)
        print("Vida del enemigo: ", enemigo.vida_enemigo, "\n")
        
        def turno_jugador():
            accion_valida = True
            accion = input("Que quieres hacer? \n \n 1. Atacar \n 2. Defender \n 3. Usar poción \n")
            if accion == "1":
                print("\n")
                Estado = random.randint(0, 100)
                print("Estado: ", Estado)
                if Estado <= jugador.probabilidad_estado:
                    enemigo.estado_enemigo = "envenenado"
                    print("El estado del enemigo es", enemigo.estado_enemigo)
                else:
                    print("Fallo estado")
                    
                Critico = random.randint(0, 100)
                print("Crítico: ", Critico)
                
                Critico_asertado = False
                if Critico <= jugador.probabilidad_critico:
                    jugador.daño_jugador *= 2
                    Critico_asertado = True
                    print("¡Crítico!")
                else:
                    print("Fallo")
                enemigo.vida_enemigo -= jugador.daño_jugador
                if Critico_asertado:
                    jugador.daño_jugador //= 2
                    Critico_asertado = False
                
                print("El jugador ataca y hace ", jugador.daño_jugador, " de daño")
                time.sleep(2.5)
            elif accion == "2":
                print("\n")
                jugador.vida_jugador += enemigo.daño_enemigo
                print("El jugador se defiende y recibe ", enemigo.daño_enemigo, " de daño")
                time.sleep(1.2)
            elif accion == "3":
                print("\n")
                if jugador.inventario["pocion"] > 0:
                    jugador.vida_jugador += 50
                    jugador.inventario["pocion"] -= 1
                    print(f"El jugador usa una poción! La vida del jugador ahora es {jugador.vida_jugador}")
                else:
                    print("No tienes pociones en tu inventario")
                    accion_valida = False
                time.sleep(1.2)
            else:
                print("Comando no válido")
                accion_valida = False
                time.sleep(1)
            return accion_valida

        def turno_enemigo():
            print("El Moustro ataca y hace ", enemigo.daño_enemigo, " de daño")
            
            jugador.vida_jugador -= enemigo.daño_enemigo
            time.sleep(1.5)
            limpar_pantalla()

        if turno == 1:
            accion_valida = turno_jugador()
            limpar_pantalla()
            if accion_valida:
                turno = 2
        elif turno == 2:
            if enemigo.estado_enemigo == "envenenado":
                enemigo.vida_enemigo -= 5
                print("enemigo envenenado sufrio 5 de daño")
                time.sleep(1)
            turno_enemigo()
            turno = 1

        if jugador.vida_jugador <= 0:
            limpar_pantalla()
            print("Has perdido")
            time.sleep(2)
            break
        elif enemigo.vida_enemigo <= 0:
            limpar_pantalla()
            print("Has ganado")
            time.sleep(2)
            break
    except Exception as e:
        print(f"An error occurred: {e}")
        break