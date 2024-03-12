from personaje import Personaje
import random
print("¡Bienvenido a Gran Fantasía!")
nombre = input("Por favor indique nombre de su personaje:\n")

jugador = Personaje(nombre)
print(jugador.estado)


orco = Personaje("Orco")

probabilidad = jugador.probabilidad_ganar(orco)

opcion_ingreso = Personaje.dialogo(probabilidad)

while opcion_ingreso == 1:
    
    atacar = random.uniform(0.0,1.0)

    if(atacar <= probabilidad):
        print("""¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!""")
        jugador.estado = 50
        orco.estado =-30
    else:
        print("""¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!""")
        jugador.estado = -30
        orco.estado =50
    print(jugador.estado)
    print(orco.estado)
    
    
    opcion_ingreso = Personaje.dialogo(probabilidad)