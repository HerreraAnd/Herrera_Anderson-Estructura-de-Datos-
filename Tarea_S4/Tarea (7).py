class GestorPersonas:
    def __init__(self):
        self.personas={}
    def agregar_personas(self, nombre, edad):
        self.personas[nombre]=edad
    def personas_mayores(self, edad_minima):
        mayores=[]
        for nombre, edad in self.personas.items():
            if edad>=edad_minima:
                mayores.append(nombre)
        return mayores
c=GestorPersonas()
c.agregar_personas("Ana", 30)
c.agregar_personas("Marcos", 15)
c.agregar_personas("Juan", 20)
print(c.personas_mayores(18))
