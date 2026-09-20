class Equipos:
    def __init__(self):
        self.lista_equipos={}
    def crear_equipo(self, nombre_equipo):
        self.lista_equipos[nombre_equipo]=[]
    def agregar_jugador(self,equipo, jugador):
        if equipo in self.lista_equipos:
            self.lista_equipos[equipo].append(jugador)
    def equipo_mayor_integrantes(self):
        equipo_mayor=max(self.lista_equipos, key=lambda eq: len(self.lista_equipos[eq]))
        return equipo_mayor

x=Equipos()
x.crear_equipo("Equipo_1")
x.crear_equipo("Equipo_2")
x.agregar_jugador("Equipo_1", "Juan")
x.agregar_jugador("Equipo_2", "Pedro")
x.agregar_jugador("Equipo_2", "Carlos")
print(x.equipo_mayor_integrantes())