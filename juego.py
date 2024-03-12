from personaje import Personaje
import random
print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje:\n")

#Se crea jugador (nueva instancia)
jugador = Personaje(nombre)
print(jugador.estado)

#Se crea Orco (nueva instancia)
orco = Personaje("Orco")

#Se consulta probabilidad de ganar
probabilidad = jugador.probabilidad_ganar(orco)

#Se usa método estatico para entregar información y pedir opción
opcion_ingreso = Personaje.dialogo(probabilidad)

#Juega hasta que escoja la opción 2 (Huir)
while opcion_ingreso == 1:

    atacar = random.uniform(0.0,1.0)

    if(atacar <= probabilidad):
        print("""¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!""")
        #Setter
        jugador.estado = 50
        orco.estado =-30
    else:
        print("""¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!""")
        #Setter
        jugador.estado = -30
        orco.estado =50
        
    #Getter
    print(jugador.estado)
    print(orco.estado)
    
    #Se usa método estatico para volver a entregar información y pedir opción
    opcion_ingreso = Personaje.dialogo(probabilidad)