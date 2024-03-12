class Personaje:
    def __init__(self,nombre : str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    @property   
    def estado(self):
        return f"""NOMBRE: {self.nombre}     NIVEL: {self.nivel}     EXP: {self.experiencia}"""
    
    @estado.setter
    def estado(self, exp):
        
        experiencia = self.experiencia + exp #Suma experiencia actual mas la ganada (o perdida)
        cambio_nivel = experiencia // 100 #puede ser positivo o negativo, es decir, subir o bajar nivel
        resto_exp = experiencia % 100 #Devuelve el resto de puntos que se debe almacenar

        self.nivel += cambio_nivel #Se realiza el cambio de nivel
        if(cambio_nivel>=0): #Si sube de nivel
            self.experiencia = resto_exp #Se asigna la experiencia restante
        else:
            self.experiencia = 0 #se vuelve experiencia a 0
            
        if(self.nivel<=0): #Si al cambiar de nivel se queda en 0 o negativo, se asigna nivel minimo (1)
            self.nivel = 1
            self.experiencia = 0
            
    def __eq__(self, other):
        return self.nivel == other.nivel
    
    def __lt__(self, other):
        return self.nivel < other.nivel
    
    def __gt__(self, other):
        return self.nivel > other.nivel
    
    def probabilidad_ganar(self,other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.50
        
    @staticmethod
    def dialogo(probabilidad):
        print("\n¡Oh no!, ¡Ha aparecido un Orco!")
        print(f'''Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n''')
        opcion_ingreso = int(input('''¿Qué deseas hacer?
1. Atacar
2. Huir\n'''))
        return opcion_ingreso