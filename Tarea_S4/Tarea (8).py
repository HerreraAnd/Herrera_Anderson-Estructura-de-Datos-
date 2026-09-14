class Equipos:
    def __init__(self):
        self.equipos={}
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo]=[]
        return nombre_equipo
    def agregar_jugador(self, nombre_equipo, jugador):
            if nombre_equipo in self.equipos:
             self.equipos[nombre_equipo].append(jugador)
            else:
                print ("El equipo no existe")
eq=Equipos()
print(eq.crear_equipo("Nombre de equipo_1"))
eq.agregar_jugador("Nombre de equipo_1", "Juan")
eq.agregar_jugador("Nombre de equipo_1", "Pedro")
print(eq.equipos)