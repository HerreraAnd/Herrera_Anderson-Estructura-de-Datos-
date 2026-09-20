class GestorPersonas:
    def __init__(self):
        self.lista_personas={}
    def agregar_personas(self, persona, edad):
        self.lista_personas[persona]=edad
    def personas_mayores(self, edad_minima):
        mayores={}
        for persona, edad in self.lista_personas.items():
            if edad>=edad_minima:
                mayores[persona]=edad
        return mayores
    def promedio(self):
        return sum(self.lista_personas.values())/len(self.lista_personas.values())
x=GestorPersonas()
x.agregar_personas("Ana", 10)
x.agregar_personas("Juan", 20)
x.agregar_personas("Homero", 38)
print(x.personas_mayores(18))
print(x.promedio())