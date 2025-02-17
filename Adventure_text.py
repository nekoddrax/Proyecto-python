import os
import time
def limpar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
arte_ascii = """
  ___      _                 _                _____         _   
 / _ \    | |               | |              |_   _|       | |  
/ /_\ \ __| |_   _____ _ __ | |_ _   _ _ __    | | _____  _| |_ 
|  _  |/ _` \ \ / / _ \ '_ \| __| | | | '__|   | |/ _ \ \/ / __|
| | | | (_| |\ V /  __/ | | | |_| |_| | |      | |  __/>  <| |_ 
\_| |_/\__,_| \_/ \___|_| |_|\__|\__,_|_|      \_/\___/_/\_\\__|
                                                                
                                                                
"""
#w
#menu de inicio del juego
def mostrar_menu():
    print(arte_ascii)
    print ("Bienvenido a \"Adventure Text\"")
    time.sleep(2)
    print("Hola este es un videojuego proyecto en base a texto en python, \n ideal para que funcione hasta en la más tostadora de las tostadoras y en lo posible en cualquier \n sistema que soporte python 3")
    time.sleep(4)
    print("¿cómo funciona el menú?")
    time.sleep(2)
    print("escribe el número de la opción en la que deseas elegir dentro del menú y luego presione ENTER ")
    time.sleep(2)
    opcion =input("Eligue una opción: \n 1. Jugar \n 2. Saber más \n 3. Salir \n")

    if opcion == "1":
        print("Jugar")
    
    elif opcion == "2":
        limpar_pantalla()
        print("Saber más")
        print("este es un juego realizado por nekoddrax \n proyecto con la finalidad de aprender a programar en python de forma personal :D \n este juego esta planeado que sea gratuito y de código abierto \n para que puedan usar de ejemplo y aprender algunas cosas, \n y/o simplemente criticar de forma contructiva tambien sirve \n")
        input("presiona enter para volver al menú")
        limpar_pantalla()
        mostrar_menu()   
    elif opcion == "3":
        limpar_pantalla()
        print("Adios :D")
        time.sleep(3)
        exit()
# llamado de la funcion 
mostrar_menu()