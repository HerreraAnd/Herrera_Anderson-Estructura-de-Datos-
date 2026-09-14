class Analizadortexto:
    def __init__(self):
        self.texto=[]
        self.palabras_unicas=set()
    def agregar_palabras(self, palabra):
        self.palabras_unicas.add(palabra)
        self.texto.append(palabra)
    def contar_palabras(self):
        return len(self.palabras_unicas)
    def agregar_multiples_palabras(self, *args):
        for palabra in args:
            self.agregar_palabras(palabra)
analizar=Analizadortexto()
analizar.agregar_multiples_palabras("texto", "prueba", "hola")
print(analizar.contar_palabras())   